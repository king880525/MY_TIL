# Linux C - Netlink API
netlink - 커널과 사용자 공간 간의 통신(AF_NETLINK)
## 개요 
``` c
#include < asm/types.h >
#include < sys/socket.h >
#include < linux/netlink.h >

netlink_socket = socket(AF_NETLINK,  socket_type ,  netlink_family );
```
## 설명
- Netlink는 커널과 사용자 공간 프로세스 간에 정보를 전송하는 데 사용
- 사용자 공간 프로세스를 위한 표준 소켓 기반 인터페이스와 커널 모듈을 위한 내부 커널 API로 구성 
- Netlink는 데이터그램 지향 서비스
- SOCK_RAW 및 SOCK_DGRAM 모두 socket_type 에 유효 
- netlink 프로토콜은 데이터그램과 원시 소켓을 구분하지 않습니다.
- netlink_family 는 통신할 커널 모듈 또는 netlink 그룹을 선택. 
## 종류
### NETLINK_ROUTE
라우팅 및 링크 업데이트를 수신하고 라우팅 테이블(IPv4 및 IPv6 모두), IP 주소, 링크 매개변수, 인접 설정, 대기열 규칙, 트래픽 클래스 및 패킷 분류자를 수정하는 데 사용
### NETLINK_W1
1-와이어 서브시스템의 메시지.
### NETLINK_USERSOCK
사용자 모드 소켓 프로토콜용으로 예약
### NETLINK_FIREWALL
netfilter에서 사용자 공간으로 IPv4 패킷을 전송합니다. ip_queue 커널 모듈에서 사용
### NETLINK_INET_DIAG
INET 소켓 모니터링.
### NETLINK_NFLOG
Netfilter/iptables ULOG.
### NETLINK_XFRM
IPsec.
### NETLINK_SELINUX
SELinux 이벤트 알림.
### NETLINK_ISCSI
개방형 iSCSI.
### NETLINK_FIB_LOOKUP
사용자 공간에서 FIB 조회에 액세스합니다.
### NETLINK_CONNECTOR
커널 커넥터. 자세한 내용 은 Linux 커널 소스 트리의 Documentation/connector/* 를 참조
### NETLINK_NETFILTER
넷필터 하위 시스템.
### NETLINK_IP6_FW
netfilter에서 사용자 공간으로 IPv6 패킷을 전송합니다. ip6_queue 커널 모듈에서 사용
### NETLINK_DNRTMSG
DECnet 라우팅 메시지.
### NETLINK_KOBJECT_UEVENT
사용자 공간에 대한 커널 메시지.
### NETLINK_GENERIC
단순화된 넷링크 사용을 위한 일반 넷링크 제품군.
## netlink 메시지
- Netlink 메시지는 하나 이상의 nlmsghdr 헤더 및 관련 페이로드가 있는 바이트 스트림으로 구성
- 바이트 스트림은 표준 NLMSG_* 매크로로만 액세스
- 멀티파트 메시지( 하나의 바이트 스트림에 연관된 페이로드가 있는 여러 nlmsghdr 헤더)에서 NLMSG_DONE 유형의 마지막 헤더를 제외하고 첫 번째 및 모든 다음 헤더에는 NLM_F_MULTI 플래그가 설정
- nlmsghdr + 페이로드 구성
``` c
struct nlmsghdr { 
    __u32 nlmsg_len; /* 헤더를 포함한 메시지의 길이. */ 
    __u16 nlmsg_type; /* 메시지 내용의 유형. */ 
    __u16 nlmsg_flags; /* 추가 플래그. */ 
    __u32 nlmsg_seq; /* 시퀀스 번호. */ 
    __u32 nlmsg_pid; /* 발신자 포트 ID. */ 
};
```
- nlmsg_type 은 표준 메시지 유형 중 하나
- NLMSG_NOOP 메시지는 무시
- NLMSG_ERROR 메시지는 오류 신호를 보내고 페이로드에는 nlmsgerr 구조가 포함 
- NLMSG_DONE 메시지는 다중 부분 메시지를 종료
``` c
struct nlmsgerr { 
    int error; /* 확인의 경우 음수 errno 또는 0 */ 
    struct nlmsghdr msg; /* 오류를 일으킨 메시지 헤더 */ 
};
```
- nlmsg_seq 및 nlmsg_pid 는 메시지를 추적하는 데 사용
- nlmsg_pid 는 메시지의 출처를 보여줍니다. 
- NLM_F_ATOMIC 에는 CAP_NET_ADMIN 기능 또는 유효 UID 0이 필요 합니다.

## 특징
- Netlink는 신뢰할 수 있는 프로토콜이 아닙니다. 
- 메모리 부족 상태나 기타 오류가 발생하면 메시지를 삭제할 수 있다.
- 안정적인 전송을 위해 발신자는 NLM_F_ACK 플래그를 설정하여 수신자에게 승인을 요청 가능. 
- 승인은 오류 필드가 0으로 설정된 NLMSG_ERROR 패킷입니다. 
- 커널은 모든 실패한 패킷에 대해 NLMSG_ERROR 메시지를 보내려고 시도
- 커널에서 사용자로의 안정적인 전송은 어떤 경우에도 불가능
- 소켓 버퍼가 가득 차면 커널은 netlink 메시지를 보낼 수 없습니다. 
- 어플리케이션에서 recvmsg에서 반환된 ENOBUFS 오류를 통해 이를 감지하고 재동기화할 수 있다.
## struct sockaddr_nl
- 사용자 공간 또는 커널에서 넷링크 클라이언트를 설명합니다. 
- 유니캐스트(하나 의 피어에게만 전송됨) 또는 넷링크 멀티캐스트 그룹( nl_groups 가 0이 아님)으로 전송될 수 있습니다.
``` c
struct sockaddr_nl { 
    sa_family_t nl_family; /* AF_NETLINK */ 
    unsigned short nl_pad; /* 영. */ 
    pid_t nl_pid; /* 포트 ID. */ 
    __u32 nl_groups; /* 멀티캐스트 그룹 마스크. */ 
};
```
### nl_pid
- 넷링크 소켓의 유니캐스트 주소
- 대상이 커널에 있으면 항상 0 
- 사용자 공간 프로세스의 경우 nl_pid 는 일반적으로 대상 소켓을 소유한 프로세스의 PID 
- nl_pid 는 프로세스가 아닌 넷링크 소켓을 식별
- 프로세스가 여러 개의 넷링크 소켓을 소유하는 경우 nl_pid 는 최대 하나의 소켓에 대한 프로세스 ID와만 같을 수 있습니다.
### nl_pid 를 netlink 소켓 에 할당하는 방법
1. 응용 프로그램이 bind (2) 를 호출하기 전에 nl_pid 를 설정
2. 응용 프로그램이 0으로 설정하면 커널이 할당을 처리
   1. 커널은 프로세스가 여는 첫 번째 넷링크 소켓에 프로세스 ID를 할당
   2. 이후에 생성되는 모든 넷링크 소켓에 고유한 nl_pid 를 할당

### nl_groups
- 모든 비트가 넷링크 그룹 번호를 나타내는 비트 마스크
- 각 넷링크 제품군에는 32개의 멀티캐스트 그룹 세트가 있습니다. 
- 소켓에서 bind가 호출되면 수신 대기하려는 그룹의 비트 마스크로 설정 
- 기본값은 멀티캐스트가 수신되지 않음을 의미하는 0
- sendmsg를 호출하거나 연결을 수행 할 때 보내려는 그룹의 비트 마스크로 nl_groups 를 설정하여 멀티캐스트 그룹에 메시지를 멀티캐스트할 수 있다.
- 유효 UID가 0 또는 CAP_NET_ADMIN 인 프로세스는 넷링크 멀티캐스트 그룹을 보내거나 수신할 수 있습니다. 
- 메시지를 여러 그룹에 브로드캐스트할 수 없습니다. 
- 멀티캐스트 그룹에 대해 수신된 메시지에 대한 모든 응답은 송신 PID와 멀티캐스트 그룹으로 다시 보내져야 합니다. 
- 일부 Linux 커널 하위 시스템은 추가로 다른 사용자가 메시지를 보내거나 받을 수 있도록 허용할 수 있습니다. 
-  NETLINK_KOBJECT_UEVENT , NETLINK_GENERIC , NETLINK_ROUTE 및 NETLINK_SELINUX 그룹을 사용하면 다른 사용자가 메시지를 받을 수 있다. 