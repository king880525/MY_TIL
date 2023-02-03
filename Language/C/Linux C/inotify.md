## inotify란
- 파일 시스템 이벤트 모니터링 모듈 
- Linux 2.6.13 커널부터 Inotify가 포함
- 파일이나 디렉토리에서 열기, 닫기, 이동/이름 변경 등 지정된 이벤트가 발생하는지 감시
## inotify API
### 1. inotify_init
- inotify 인스턴스를 작성
- 성공하면 인스턴스가 참조하는 파일 디스크립터를 리턴하는 시스템 호출
- 실패하면 -1 리턴 
- 다른 시스템 호출과 마찬가지로 실패하면 errno 확인 필요.
### 2. inotify_init1
- inotify_init와 비슷하지만 추가 플래그가 있다. 
- 플래그가 지정되지 않으면 이 함수는 inotify_init와 동일
### 3. inotify_add_watch
- 파일이나 디렉토리에 감시를 추가하며 감시할 이벤트를 지정한다. 
- 감시의 종류에 따라 플래그 설정
  - 기존 감시에 이벤트를 추가
  - 경로에 디렉토리가 표시되는 경우에만 감시를 수행 
  - 기호 링크를 수행해야 하는지 그리고 
  - 감시가 첫 번째 이벤트가 발생하면 중지되어야 하는 일회성 감시
- 성공 하면 inotify_add_watch() 호출은 등록된 시계의 고유 식별자를 반환
- 실패하면 -1을 반환
- 식별자를 사용하여 연결된 시계를 변경하거나 제거 가능
### 4. inotify_rm_watch
- 감시 목록에서 감시 항목을 제거한다.
### 5. read
- 이 함수는 하나 이상의 이벤트에 관한 정보가 포함된 버퍼를 읽는다.
### 6. close
- 파일 디스크립터를 닫고 파일 디스크립터에 남아 있는 모든 감시를 제거 
## 일반적인 모니터링 과정
1.`inotify_init`를 사용하여 파일 디스크립터를 연다.
2.하나 이상의 감시를 추가한다.(`inotify_add_watch`)
3.이벤트를 대기한다.(`read`)
4.이벤트를 처리한 후 대기 상태로 돌아간다.
5.더 이상 활성화된 감시가 없거나 어떤 신호를 수신하는 경우에는 파일 디스크립터를 닫고 정리한 후 종료된다.(`close`)
## inotify_event
``` C
struct inotify_event
{
    int wd; /* Watch descriptor. */
    uint32_t mask; /* Watch mask. */
    uint32_t cookie; /* Cookie to synchronize two events. */
    uint32_t len; /* Length (including NULs) of name. */
    char name __flexarr; /* Name. */
};
```
- name: 감시 항목이 디렉토리이고, 이벤트가 디렉토리에 있는 항목에 해당하는 경우에만 표시
- cookie: IN_MOVED_FROM 이벤트와 IN_MOVED_TO 이벤트가 감시할 항목과 관련된 경우, 두 이벤트의 연관성을 확인하기 위해 쿠키를 사용
- mask: 커널에 의해 설정되는 플래그와 함께 이벤트 유형이 리턴. 예를 들면, 이벤트 대상이 디렉토리인 경우에는 커널에서 IN_ISDIR 플래그를 설정.
## event 종류
### IN_ACCESS
- 감시 디렉토리에 있는 감시 항목이 액세스
### IN_MODIFY
- 감시 디렉토리에 있는 감시 항목이 수정
### IN_ATTRIB
- 감시 디렉토리에 있는 감시 항목에서 메타 데이터가 변경. 예를 들면, 시간소인이나 사용 권한이 변경된 경우
### IN_CLOSE_WRITE
- 쓰기 위해 연 파일이나 디렉토리가 닫혔다.
### IN_CLOSE_NOWRITE
- 읽기 전용으로 연 파일이나 디렉토리가 닫혔다.
### IN_CLOSE
- 이전의 두 가지 닫기 이벤트(IN_CLOSE_WRITE | IN_CLOSE_NOWRITE)를 논리적 OR 연산
### IN_OPEN
- 파일이나 디렉토리가 열렸다.
### IN_MOVED_FROM
- 감시 디렉토리에 있는 감시 항목이 감시 위치에서 이동.
- 이 이벤트에는 쿠키가 포함
- 사용자는 쿠키를 이용하여 IN_MOVED_FROM와 IN_MOVED_TO의 연관성을 확인 가능
### IN_MOVED_TO
- 0파일이나 디렉토리가 감시 위치에서 이동
- 이 이벤트에는 IN_MOVED_FROM과의 연관성을 확인할 수 있는 쿠키가 포함
- 파일이나 디렉토리의 이름이 변경되면 두 가지 이벤트가 모두 표시
- 파일이나 디렉토리가 감시하고 있지 않은 위치로 이동하거나 이 위치에서 이동되는 경우에는 한 가지 이벤트만 표시
- 사용자가 감시 항목을 이동하거나 이름을 변경하는 경우에도 감시는 계속된다. 
- IN_MOVE-SELF 참조
### IN_MOVE
- 두 가지 이동 이벤트(IN_MOVED_FROM | IN_MOVED_TO)를 논리적 OR 연산
### IN_CREATE
- 서브디렉토리나 파일이 감시 디렉토리에서 작성
### IN_DELETE
- 서브디렉토리나 파일이 감시 디렉토리에서 삭제
### IN_DELETE_SELF
- 감시 항목 자체가 삭제
- 감시가 종료되고 IN_IGNORED 이벤트를 수신
### IN_MOVE_SELF
- 감시 항목 자체가 이동
### 기타
- 이벤트 플래그 외에도 사용자가 Inotify 헤더(/usr/include/sys/inotify.h)에서 찾을 수 있는 몇 가지 다른 플래그가 있다. 
- 첫 번째 이벤트만 감시하려고 하는 경우에는 감시를 추가할 때 IN_ONESHOT 플래그를 설정
## example 코드
``` c
void signal_handler (int signum)
{
    keep_running = 0;
}

int main (int argc, char **argv)
{
    int inotify_fd;

    keep_running = 1;

    if (signal (SIGINT, signal_handler) == SIG_IGN) {
        signal (SIGINT, SIG_IGN);
    }

    inotify_fd = open_inotify_fd (); 
    if (inotify_fd > 0) {
        int wd; 
        int index;
        queue_t q;

        q = queue_create (128);

        wd = 0;
        printf("\n");
        for (index = 1; (index < argc) && (wd >= 0); index++) {
            wd = watch_dir (inotify_fd, argv[index], IN_ALL_EVENTS);
        }

        if (wd > 0) {
            process_inotify_events (q, inotify_fd);
        }
        printf ("\nTerminating\n");

        close_inotify_fd (inotify_fd);
        queue_destroy (q);
    }
    return 0;
}
```
## inotifywait
리눅스에서 지원하는 inotifywait 커맨드를 이용하는 방법도 있다.
ex)
터미널 1
``` bash
# touch cheese
# while inotifywait -e modify cheese; do 
>   echo someone touched my cheese
> done
```
터미널 2
``` bash
echo lol >> cheese
```
결과
``` bash
Setting up watches.
Watches established.
cheese MODIFY 
someone touched my cheese
Setting up watches.
Watches established.
```
