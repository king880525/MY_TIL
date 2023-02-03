# 1. 개요
- poll은 select 와 마찬가지로 다중입출력 을 구현하기 위한 방법으로 사용
- 동시에 여러개의 클라이언트를 다루는 서버를 제작하기 위한 방법으로 흔히 사용된다.
- select 의 경우 입출력 이벤트가 발생했을 때 넘겨주는 정보가 너무 적음으로써, 프로그래밍시 여기에 신경을 써줘야 하는데 poll 을 이용하면 이러한 제한을 극복할수 있다.
# 2. 정의
## poll
``` C
int poll(struct poolfd *ufds, unsigned int nfds, int timeout);
```
[poll이 여러개의 파일을 다루는 방법] 
- select 와 마찬가지로 파일지시자의 이벤트를 기다리다가 이벤트가 발생
- poll 에서의 block 이 해제되고, 다음 루틴에서 어떤 파일지시자에 이벤트가 발생했는지 검사
## pollfd
``` C
struct pollfd
{
	int fd;         // 관심있어하는 파일지시자
	short events;   // 발생된 이벤트
	short revents;  // 돌려받은 이벤트
};
```
fd - 파일 디스크립터
events - 파일 디스크립터가 발생시키는 이벤트
revents - 커널에서 이 events 에 어떻게 반응 했는지에 대한 반응 값이다.
## events
`<sys/poll.h>` 에 디파인 되어 있다.
``` c
    #define POLLIN      0x0001  // 읽을 데이타가 있다.
    #define POLLPRI     0x0002  // 긴급한 읽을 데이타가 있다.
    #define POLLOUT     0x0004  // 쓰기가 봉쇄(block)가 아니다. 
    #define POLLERR     0x0008  // 에러발생
    #define POLLHUP     0x0010  // 연결이 끊겼음
    #define POLLNVAL    0x0020  // 파일지시자가 열리지 않은것같은 Invalid request (잘못된 요청)
```
## nfds
- pollfd 의 배열의 크기
- 우리가 조사할 파일지시자의 크기(네트웍프로그래밍측면에서 보자면 받아들일수 있는 클라이언트의 크기)
- 보통 프로그래밍 할때 그 크기를 지정해준다.
## timeout
- select 의 time 와 같은 역할
- 값을 지정하지 않을경우 이벤트가 발생하기 전까지 영원히 기다린다.
- 0일 경우는 기다리지 않고 곧바로 다음 루틴을 진행
- 0보다 큰 양의 정수일 경우에는 해당 시간만큼을 기다리게 된다. 
- 해당 시간내에 어떤 이벤트가 발생하면 즉시 되돌려 주며, 시간을 초과하게 될 경우 0을 return 한다.
# 3. example
``` c
#include <sys/time.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#include <sys/stat.h> 
#include <unistd.h> 
#include <stdlib.h> 
#include <stdio.h> 
#include <string.h> 
#include <netinet/in.h> 
#include <arpa/inet.h> 
#include <sys/poll.h> 

// 받아들일수 있는 클라이언트의 크기
#define OPEN_MAX    600 

int main(int argc, char **argv)
{

    int server_sockfd, client_sockfd, sockfd;

    int i, maxi;
    int nread;
    int state = 0;

    socklen_t clilen;

    struct sockaddr_in clientaddr, serveraddr;

    char buf[255];
    char line[255];

    FILE *fp;

    struct pollfd client[OPEN_MAX];

    if (argc != 2)
    {
        printf("Usage : ./zipcode_poll [port]\n");
        printf("예    : ./zipcode_poll 4444\n");
        exit(0);
    }


    if ((fp = fopen("zipcode.txt", "r")) == NULL)
    {
        perror("file open error : ");
        exit(0);
    }

    if ((server_sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("socket error : ");
        exit(0);
    }
    bzero(&serveraddr, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    serveraddr.sin_addr.s_addr = htonl(INADDR_ANY);
    serveraddr.sin_port = htons(atoi(argv[1]));

    state = bind(server_sockfd, (struct sockaddr *)&serveraddr, 
                sizeof(serveraddr));

    if (state == -1)
    {
        perror("bind error : ");
        exit(0);
    }
    state = listen(server_sockfd, 5);
    if (state == -1)
    {
        perror("listen error : ");
        exit(0);
    }

    // pollfd  구조체에 
    // 소켓지시자를 할당한다.  
    // 소켓에 쓰기 events (POLLIN)에 대해서 
    // 반응하도록 세팅한다. 
    client[0].fd = server_sockfd;
    client[0].events = POLLIN;

    // pollfd 구조체의 모든 fd 를 -1 로 초기화 한다.  
    // fd 가 -1 이면 파일지시자가 세팅되어있지 않다는 뜻이다. 
    for (i = 1; i < OPEN_MAX; i++)
    {
        client[i].fd = -1;
    }
    maxi = 0;

    // POLLING 시작
    for (;;)
    {
        nread = poll(client, maxi + i, 1000);

        // 만약 POLLIN 이벤트에 대해서 
        // 되돌려준 이벤트가(revents) POLLIN
        // 이라면 accept 한다. 
        if (client[0].revents & POLLIN)
        {
            clilen=sizeof(clientaddr);
            client_sockfd = accept(server_sockfd, 
                            (struct sockaddr *)&clientaddr, 
                            &clilen);
            for (i = 1; i < OPEN_MAX; i++)
            {
                if (client[i].fd < 0)
                {
                    client[i].fd = client_sockfd;
                    break;
                }
            }

            if (i == OPEN_MAX)
            {
                perror("too many clients : ");
                exit(0);
            }

            client[i].events = POLLIN;

            if (i > maxi)
            {
                maxi = i;
            }

            if (--nread <= 0)
                continue;
        }

        // 현재 파일지시자의 총갯수 만큼 루프를 돌면서 
        // 각 파일지시자에 POLLIN revent 가 발생했는지를 조사하고 
        // POLLIN이 발생했다면, 해당 파일지시자에서 데이타를 읽어들이고, 
        // 주소정보를 돌려준다. 
        // 만약 "quit" 를 읽었다면, 소켓연결을 끊는다. 
        for (i = 1; i <= maxi; i++)
        {
            if ((sockfd = client[i].fd) < 0)
                continue;
            if (client[i].revents & (POLLIN | POLLERR))
            {
                rewind(fp);
                memset(buf, 0x00, 255);
                if (read(sockfd, buf, 255) <= 0)
                {
                    close(client[i].fd);
                    client[i].fd = -1;
                }
                else
                {
                    if (strncmp(buf, "quit", 4) == 0)
                    {
                        write(sockfd, "byebye\n", 7);
                        close(client[i].fd);
                        client[i].fd = -1;
                        break;
                    }
                    while(fgets(line, 255, fp) != NULL)
                    {
                        if (strstr(line, buf) != NULL)
                            write(sockfd, line, 255);
                        memset(line, 0x00, 255);
                    }
                }
            }
        }
    }
}
```