# Linux C - netdevice API
netdevice - Linux 네트워크 장치에 대한 저수준 액세스
## 개요
``` c
#include < sys/ioctl.h >
#include < net/if.h >
```
## 설명
Linux는 네트워크 장치를 구성하기 위해 일부 표준 ioctl을 지원합니다. 
패밀리나 유형에 관계없이 모든 소켓의 파일 설명자에서 사용할 수 있습니다. 
그들은 ifreq 구조를 전달합니다:
``` c
struct ifreq {
    char ifr_name[IFNAMSIZ]; /* Interface name */
    union {
        struct sockaddr ifr_addr;
        struct sockaddr ifr_dstaddr;
        struct sockaddr ifr_broadaddr;
        struct sockaddr ifr_netmask;
        struct sockaddr ifr_hwaddr;
        short           ifr_flags;
        int             ifr_ifindex;
        int             ifr_metric;
        int             ifr_mtu;
        struct ifmap    ifr_map;
        char            ifr_slave[IFNAMSIZ];
        char            ifr_newname[IFNAMSIZ];
        char           *ifr_data;
    };
};

struct ifconf {
    int                 ifc_len; /* size of buffer */
    union {
        char           *ifc_buf; /* buffer address */
        struct ifreq   *ifc_req; /* array of structures */
    };
};
```
일반적으로 사용자는 ifr_name 을 인터페이스 이름으로 설정하여 영향을 줄 장치를 지정합니다. 구조의 다른 모든 구성원은 메모리를 공유할 수 있습니다.
## Ioctls
ioctl이 권한 있는 것으로 표시된 경우 이를 사용하려면 유효 사용자 ID 0 또는 CAP_NET_ADMIN 기능이 필요합니다. 그렇지 않은 경우 EPERM 이 반환됩니다.
### SIOCGIFNAME
ifr_ifindex 가 주어지면 ifr_name 의 인터페이스 이름을 반환합니다 . 이것은 ifr_name 에 결과를 반환하는 유일한 ioctl입니다 .
### SIOCGIFINDEX
인터페이스의 인터페이스 인덱스를 ifr_ifindex 로 검색합니다 .
### SIOCGIFFLAGS , SIOCSIFFLAGS
장치의 활성 플래그 단어를 가져오거나 설정합니다. ifr_flags 는 다음 값의 비트 마스크를 포함합니다.
활성 플래그 단어를 설정하는 것은 권한이 있는 작업이지만 모든 프로세스에서 읽을 수 있습니다.
### SIOCGIFPFLAGS , SIOCSIFPFLAGS
장치에 대한 확장(비공개) 플래그를 가져오거나 설정합니다. ifr_flags 는 다음 값의 비트 마스크를 포함합니다.
확장(개인) 인터페이스 플래그를 설정하는 것은 권한이 있는 작업입니다.
### SIOCGIFADDR , SIOCSIFADDR
ifr_addr 을 사용하여 장치의 주소를 가져오거나 설정합니다 . 인터페이스 주소 설정은 권한이 있는 작업입니다. 호환성을 위해 AF_INET 주소만 허용되거나 반환됩니다.
### SIOCGIFDSTADDR , SIOCSIFDSTADDR
ifr_dstaddr 을 사용하여 지점간 장치의 대상 주소를 가져오거나 설정합니다 . 호환성을 위해 AF_INET 주소만 허용되거나 반환됩니다. 대상 주소를 설정하는 것은 권한이 있는 작업입니다.
### SIOCGIFBRDADDR , SIOCSIFBRDADDR
ifr_brdaddr 을 사용하여 장치의 브로드캐스트 주소를 가져오거나 설정합니다 . 호환성을 위해 AF_INET 주소만 허용되거나 반환됩니다. 브로드캐스트 주소 설정은 권한이 있는 작업입니다.
### SIOCGIFNETMASK , SIOCSIFNETMASK
ifr_netmask 를 사용하여 장치의 네트워크 마스크를 가져오거나 설정합니다 . 호환성을 위해 AF_INET 주소만 허용되거나 반환됩니다. 네트워크 마스크 설정은 권한이 있는 작업입니다.
### SIOCGIFMETRIC , SIOCSIFMETRIC
ifr_metric 을 사용하여 장치의 메트릭을 가져오거나 설정합니다 . 이것은 현재 구현되지 않았습니다. 읽기를 시도하면 ifr_metric 을 0으로 설정하고 설정을 시도하면 EOPNOTSUPP를 반환 합니다 .
### SIOCGIFMTU , SIOCSIFMTU
ifr_mtu 를 사용하여 장치의 MTU(최대 전송 단위)를 가져오거나 설정합니다 . MTU 설정은 권한이 있는 작업입니다. MTU를 너무 작은 값으로 설정하면 커널 충돌이 발생할 수 있습니다.
### SIOCGIFHWADDR , SIOCSIFHWADDR
ifr_hwaddr 을 사용하여 장치의 하드웨어 주소를 가져오거나 설정합니다 . 하드웨어 주소는 struct sockaddr 에 지정됩니다 . sa_family 는 ARPHRD_* 장치 유형을 포함하고 sa_data 는 바이트 0부터 시작하는 L2 하드웨어 주소를 포함합니다. 하드웨어 주소 설정은 권한이 있는 작업입니다.
### SIOCSIFHWBROADCAST
ifr_hwaddr 에서 장치의 하드웨어 브로드캐스트 주소를 설정합니다 . 이것은 권한이 있는 작업입니다.
### SIOCGIFMAP , SIOCSIFMAP
ifr_map 을 사용하여 인터페이스의 하드웨어 매개변수를 가져오거나 설정합니다 . 매개변수 설정은 권한이 있는 작업입니다.
``` c
struct ifmap {
    unsigned long   mem_start;
    unsigned long   mem_end;
    unsigned short  base_addr;
    unsigned char   irq;
    unsigned char   dma;
    unsigned char   port;
};
```
ifmap 구조의 해석은 장치 드라이버와 아키텍처에 따라 다릅니다.
### SIOCADDMULTI , SIOCDELMULTI
ifr_hwaddr 을 사용하여 장치의 링크 레이어 멀티캐스트 필터에 주소를 추가하거나 삭제합니다 . 권한 있는 작업입니다. 대안은 패킷 (7)을 참조하십시오 .
### SIOCGIFTXQLEN , SIOCSIFTXQLEN
ifr_qlen 을 사용하여 장치의 전송 큐 길이를 가져오거나 설정합니다 . 전송 큐 길이 설정은 권한이 있는 작업입니다.
### SIOCSIFNAME
ifr_name에 지정된 인터페이스의 이름을 ifr_newname 으로 변경 합니다. 이것은 권한이 있는 작업입니다. 인터페이스가 작동하지 않을 때만 허용됩니다.
### SIOCGIFCONF
인터페이스(전송 계층) 주소 목록을 반환합니다. 이것은 현재 호환성을 위해 AF_INET (IPv4) 제품군의 주소만 의미합니다. 사용자는 ifconf 구조를 ioctl에 대한 인수로 전달합니다. 여기에는 ifc_req 의 ifreq 구조 배열에 대한 포인터 와 ifc_len 의 바이트 단위 길이가 포함됩니다 . 커널은 실행 중인 모든 현재 L3 인터페이스 주소로 ifreq를 채웁니다. ifr_name 은 인터페이스 이름(eth0:1 등)을 포함하고 ifr_addr 은 주소를 포함합니다. 커널은 ifc_len 의 실제 길이와 함께 반환됩니다 . ifc_len인 경우버퍼가 오버플로했을 가능성이 있는 원래 길이와 같으므로 모든 주소를 가져오려면 더 큰 버퍼로 다시 시도해야 합니다. 오류가 발생하지 않으면 ioctl은 0을 반환합니다. 그렇지 않으면 -1. 오버플로는 오류가 아닙니다.
### 기타
대부분의 프로토콜은 프로토콜별 인터페이스 옵션을 구성하기 위해 자체 ioctl을 지원합니다. 설명은 프로토콜 매뉴얼 페이지를 참조하십시오. IP 주소 구성은 ip (7)을 참조하십시오.
또한 일부 장치는 개인 ioctl을 지원합니다. 여기에 대해서는 설명하지 않습니다.
## 메모
엄밀히 말하면 SIOCGIFCONF 및 AF_INET 소켓 주소 만 수락하거나 반환하는 다른 ioctl 은 IP에 고유하며 ip (7)에 속합니다.
주소가 없거나 IFF_RUNNING 플래그가 설정 되지 않은 인터페이스의 이름은 /proc/net/dev 를 통해 찾을 수 있습니다 .
로컬 IPv6 IP 주소는 /proc/net 또는 rtnetlink (7)를 통해 찾을 수 있습니다.

# Linux C - netdevice API
netdevice - Linux 네트워크 장치에 대한 저수준 액세스
## 개요
``` c
#include < sys/ioctl.h >
#include < net/if.h >
```
## 설명
- Linux에서 네트워크 장치를 구성하기 위한 표준 ioctl 
- 패밀리나 유형에 관계없이 모든 소켓의 파일 설명자에서 사용 가능
- ioctl을 통해 struct ifreq 전달
``` c
struct ifreq {
    char ifr_name[IFNAMSIZ]; /* Interface name */
    union {
        struct sockaddr ifr_addr;
        struct sockaddr ifr_dstaddr;
        struct sockaddr ifr_broadaddr;
        struct sockaddr ifr_netmask;
        struct sockaddr ifr_hwaddr;
        short           ifr_flags;
        int             ifr_ifindex;
        int             ifr_metric;
        int             ifr_mtu;
        struct ifmap    ifr_map;
        char            ifr_slave[IFNAMSIZ];
        char            ifr_newname[IFNAMSIZ];
        char           *ifr_data;
    };
};

struct ifconf {
    int                 ifc_len; /* size of buffer */
    union {
        char           *ifc_buf; /* buffer address */
        struct ifreq   *ifc_req; /* array of structures */
    };
};
```
- 사용자는 ifr_name 을 인터페이스 이름으로 설정하여 영향을 줄 장치를 지정 
- struct의 다른 모든 member는 메모리를 공유 가능.
## Ioctls
- ioctl이 권한 있는 것으로 표시된 경우 이를 사용하려면 유효 사용자 ID 0 또는 CAP_NET_ADMIN 기능이 필요합니다. 그렇지 않은 경우 EPERM 이 반환됩니다.
### SIOCGIFNAME
- ifr_ifindex에 해당하는 ifr_name 의 인터페이스 이름 반환
- ifr_name을 반환하는 유일한 ioctl
### SIOCGIFINDEX
- 인터페이스 인덱스를 ifr_ifindex 로 검색
### SIOCGIFFLAGS , SIOCSIFFLAGS
- 장치의 활성 플래그 단어를 가져오거나 설정
- ifr_flags 는 다음 값의 비트 마스크를 포함합니다.
- 활성 플래그 단어를 설정하는 것은 권한이 있는 작업이지만 모든 프로세스에서 읽을 수 있습니다.
### SIOCGIFPFLAGS , SIOCSIFPFLAGS
- 장치에 대한 확장(비공개) 플래그를 가져오거나 설정
- ifr_flags 는 다음 값의 비트 마스크를 포함합니다.
- 확장(개인) 인터페이스 플래그를 설정하는 것은 권한이 있는 작업입니다.
### SIOCGIFADDR , SIOCSIFADDR
- ifr_addr 을 사용하여 장치의 주소를 가져오거나 설정
- 인터페이스 주소 설정은 권한이 있는 작업입니다. 
- 호환성을 위해 AF_INET 주소만 허용되거나 반환
### SIOCGIFDSTADDR , SIOCSIFDSTADDR
- ifr_dstaddr 을 사용하여 지점간 장치의 대상 주소를 가져오거나 설정
- 호환성을 위해 AF_INET 주소만 허용되거나 반환
- 대상 주소를 설정하는 것은 권한이 있는 작업입니다.
### SIOCGIFBRDADDR , SIOCSIFBRDADDR
- ifr_brdaddr 을 사용하여 장치의 브로드캐스트 주소를 가져오거나 설정
- 호환성을 위해 AF_INET 주소만 허용되거나 반환
- 브로드캐스트 주소 설정은 권한이 있는 작업입니다.
### SIOCGIFNETMASK , SIOCSIFNETMASK
- ifr_netmask 를 사용하여 장치의 네트워크 마스크를 가져오거나 설정
- 호환성을 위해 AF_INET 주소만 허용되거나 반환
- 네트워크 마스크 설정은 권한이 있는 작업입니다.
### SIOCGIFMETRIC , SIOCSIFMETRIC
- ifr_metric 을 사용하여 장치의 메트릭을 가져오거나 설정
- 이것은 현재 구현되지 않았습니다. 
- 읽기를 시도하면 ifr_metric 을 0으로 설정하고 설정을 시도하면 EOPNOTSUPP를 반환 합니다 .
### SIOCGIFMTU , SIOCSIFMTU
- ifr_mtu 를 사용하여 장치의 MTU(최대 전송 단위)를 가져오거나 설정
- MTU 설정은 권한이 있는 작업입니다. 
- MTU를 너무 작은 값으로 설정하면 kernel panic이 발생할 수 있습니다.
### SIOCGIFHWADDR , SIOCSIFHWADDR
- ifr_hwaddr 을 사용하여 장치의 하드웨어 주소를 가져오거나 설정
- 하드웨어 주소는 struct sockaddr 에 지정
- sa_family 는 ARPHRD_* 장치 유형을 포함
- sa_data 는 바이트 0부터 시작하는 L2 하드웨어 주소를 포함
- 하드웨어 주소 설정은 권한이 있는 작업입니다.
### SIOCSIFHWBROADCAST
- ifr_hwaddr 에서 장치의 하드웨어 브로드캐스트 주소를 설정
- 이것은 권한이 있는 작업입니다.
### SIOCGIFMAP , SIOCSIFMAP
- ifr_map 을 사용하여 인터페이스의 하드웨어 매개변수를 가져오거나 설정
- 매개변수 설정은 권한이 있는 작업입니다.
``` c
struct ifmap {
    unsigned long   mem_start;
    unsigned long   mem_end;
    unsigned short  base_addr;
    unsigned char   irq;
    unsigned char   dma;
    unsigned char   port;
};
```
- ifmap 구조의 해석은 장치 드라이버와 아키텍처에 따라 다릅니다.
### SIOCADDMULTI , SIOCDELMULTI
- ifr_hwaddr 을 사용하여 장치의 링크 레이어 멀티캐스트 필터에 주소를 추가하거나 삭제
- 권한 있는 작업입니다.
### SIOCGIFTXQLEN , SIOCSIFTXQLEN
- ifr_qlen 을 사용하여 장치의 전송 큐 길이를 가져오거나 설정
- 전송 큐 길이 설정은 권한이 있는 작업입니다.
### SIOCSIFNAME
- ifr_name에 지정된 인터페이스의 이름을 ifr_newname 으로 변경
- 이것은 권한이 있는 작업입니다.
- 인터페이스가 작동하지 않을 때만 허용
### SIOCGIFCONF
- 인터페이스(전송 계층) 주소 목록을 반환
- 이것은 현재 호환성을 위해 AF_INET (IPv4) 제품군의 주소만 의미
- 사용자는 ifconf 구조를 ioctl에 대한 인수로 전달
- ifc_req 의 ifreq 구조 배열에 대한 포인터 와 ifc_len 의 바이트 단위 길이가 포함
- 커널은 실행 중인 모든 현재 L3 인터페이스 주소로 ifreq를 채웁니다. 
- ifr_name 은 인터페이스 이름(eth0:1 등)을 포함 
- ifr_addr 은 주소를 포함
- 커널은 ifc_len 의 실제 길이와 함께 반환 
- ifc_len인 경우, 버퍼가 오버플로했을 가능성이 있는 원래 길이와 같으므로 모든 주소를 가져오려면 더 큰 버퍼로 다시 시도해야 합니다. 
- 오류가 발생하지 않으면 ioctl은 0을 반환합니다. 
- 그렇지 않으면 -1. 
- 오버플로는 오류가 아닙니다.
### 기타
- 대부분의 프로토콜은 프로토콜별 인터페이스 옵션을 구성하기 위해 자체 ioctl을 지원
- 일부 장치는 private ioctl을 지원
## 메모
- SIOCGIFCONF 및 AF_INET 소켓 주소 만 수락하거나 반환하는 다른 ioctl 은 ip에 속합니다.
- 주소가 없거나 IFF_RUNNING 플래그가 설정되지 않은 인터페이스의 이름은 /proc/net/dev 를 통해 찾을 수 있습니다 .
- 로컬 IPv6 IP 주소는 /proc/net 또는 rtnetlink를 통해 찾을 수 있습니다.