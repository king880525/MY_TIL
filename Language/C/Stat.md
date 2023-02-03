# 1. 개요 
파일의 상태를 가져오는 함수

# 2. 사용법
``` c
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

int stat(const char *file_name, struct stat *buf);
int fstat(int filedes, struct stat *buf);
int lstat(const char *file_name, struct stat *buf);
```
- 각 함수들의 호출 성공시 0을 반환
- 두번째 인자인 stat 구조체에 파일 정보들로 채워진다.
- 실패 혹은 에러시 -1을 리턴
- 에러시에 errno 변수에 에러 상태가 set된다.
- stat과 lstat함수는 첫번째 인자로 절대경로, 두번째 인자로 stat 구조체 주소
- lstat 함수는 path가 심볼릭 링크 파일 경우, 심볼릭 링크 파일에 대한 정보를 구조제에 채운다. (stat 함수는  원본의 정보를 채운다.)
# 3. 설명
stat() 
- 파일의 상태를 알아올수 있다. 
- 첫번째 인자로 주어진 file_name 의 상태를 얻어와서 두번째 인자인 buf 에 채워 넣는다.
lstat() 
- 심볼릭 링크 파일의 원본파일의 상태를 얻어온다는 것을 제외 하고는 stat()과 동일하다.
fstat()
- open 등을 통해서 만들어진 file descriptor를 인자로 받아들인다는 점 외에는 stat()과 동일
``` c
struct stat {
    dev_t         st_dev;      /* device */
    ino_t         st_ino;      /* inode */
    mode_t        st_mode;     /* protection */
    nlink_t       st_nlink;    /* number of hard links */
    uid_t         st_uid;      /* user ID of owner */
    gid_t         st_gid;      /* group ID of owner */
    dev_t         st_rdev;     /* device type (if inode device) */
    off_t         st_size;     /* total size, in bytes */
    blksize_t     st_blksize;  /* blocksize for filesystem I/O */
    blkcnt_t      st_blocks;   /* number of blocks allocated */
    time_t        st_atime;    /* time of last access */
    time_t        st_mtime;    /* time of last modification */
    time_t        st_ctime;    /* time of last change */
};
```
# 4. example code
``` c
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <pwd.h>
#include <grp.h>

int main(int argc, char **argv)
{
    int return_stat;
    char *file_name;
    struct stat file_info;
    struct passwd *my_passwd;
    struct group  *my_group;
    mode_t file_mode;
    
    if (argc != 2 ) {
        printf("Usage : ./file_info [file name]\n");
        exit(0);
    }
    file_name = argv[1];    

    if ((return_stat = stat(file_name, &file_info)) == -1) {
        perror("Error : ");
        exit(0);
    }

    file_mode = file_info.st_mode;
    printf("파일이름 : %s\n", file_name);
    printf("=======================================\n");
    printf("파일 타입 : ");
    if (S_ISREG(file_mode)) {
        printf("정규파일\n");
    } else if (S_ISLNK(file_mode)) {
        printf("심볼릭 링크\n");
    } else if (S_ISDIR(file_mode)) {
        printf("디렉토리\n");    
    } else if (S_ISCHR(file_mode)) {
        printf("문자 디바이스\n");
    } else if (S_ISBLK(file_mode)) {
        printf("블럭 디바이스\n");
    } else if (S_ISFIFO(file_mode)) {
        printf("FIFO\n");
    } else if (S_ISSOCK(file_mode)) {
        printf("소켓\n");
    }

    my_passwd = getpwuid(file_info.st_uid);
    my_group  = getgrgid(file_info.st_gid);
    printf("OWNER : %s\n", my_passwd->pw_name);
    printf("GROUP : %s\n", my_group->gr_name);
    printf("FILE SIZE IS : %d\n", file_info.st_size);
    printf("마지막 읽은 시간 : %d\n", file_info.st_atime);
    printf("마지막 수정 시간 : %d\n", file_info.st_mtime);
    printf("하드링크된 파일수 : %d\n", file_info.st_nlink);
}
```
# 5. 참조 링크
https://bodamnury.tistory.com/37
https://linux.die.net/man/2/stat