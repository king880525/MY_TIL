## ssh
### ssh 접속 로그 파일
```
/var/log/wtmp
/var/log/btmp
```
전체 ssh 접속 정보를 확인 가능
```
/var/log/secure
```
권한과 관련된 모든 로그가 실시간으로 업데이트(ex: sudo, ssh)
debian 계열에서는 `/var/log/auth.log`를 사용하기도 함.
### sshd 로그인 과정
로그인 과정
사용자가 성공적으로 sshd에 로그인하면 다음을 수행합니다.
1. 로그인이 tty에 있고 명령이 지정되지 않은 경우 마지막 로그인 시간과 /etc/motd 를 인쇄 합니다(구성 파일에서 또는 ~/.hushlogin 에 의해 방지되지 않는 한 , FILES 섹션 참조).
2. 로그인이 tty에 있는 경우 로그인 시간을 기록합니다.
3. /etc/nologin 확인하여 존재하는 경우 내용을 인쇄하고 종료합니다(루트가 아닌 경우).
4. 일반 사용자 권한으로 실행하도록 변경합니다.
5. 기본 환경을 설정합니다.
6. ~/.ssh/environment 파일 이 존재하는 경우 이를 읽고 사용자는 환경을 변경할 수 있습니다. sshd_config(5)PermitUserEnvironment 의 옵션을 참조하십시오 .
7. 사용자의 홈 디렉토리로 이동합니다.
8. ~/.ssh/rc 가 존재하고 sshd_config(5) PermitUserRC 옵션이 설정되어 있으면 실행합니다 . 그렇지 않으면 /etc/ssh/sshrc 가 존재하면 실행합니다. 그렇지 않으면 xauth(1) 을 실행 합니다. "rc" 파일에는 표준 입력에서 X11 인증 프로토콜과 쿠키가 제공됩니다.
9. 사용자의 셸 또는 명령을 실행합니다. 모든 명령은 시스템 암호 데이터베이스에 지정된 대로 사용자의 로그인 셸에서 실행됩니다.
### login/logout 스크립트
#### 1. ForceCommand
/etc/ssh/sshd_config 에 ForceCommand 옵션에 실행할 스크립트를 명시함으로서 실행 가능.
ForceCommand 옵션에 지정한 스크립트는 기존 SSH 실행 커맨드 및 기본 쉘을 대체한다.
ex)
``` bash
#! /bin/sh

# find IP address
ip=`echo $SSH_CONNECTION | cut -d " " -f 1`
port=`echo $SSH_CONNECTION | cut -d " " -f 2`

# Login 로그
echo "$USER login from $ip:$port"

# 기본 쉘 실행
$SHELL

# Logout 로그
echo "$USER logout from $ip:$port"
```
#### 2. sshrc
~/.ssh/rc 가 존재하고 sshd_config(5) PermitUserRC 옵션이 존재하면 
ssh 로그인할 때, 유저별 rc 커맨드 실행.
해당 옵션이 없거나 유저별 rc 커맨드가 없으면 기본적으로 ssh 접속 
/etc/ssh/sshrc 커맨드 실행.
ex)
``` bash
#!/bin/sh

if [ -n "$SSH_CONNECTION" ]; then
    ip=`echo $SSH_CONNECTION | cut -d " " -f 1`
    port=`echo $SSH_CONNECTION | cut -d " " -f 2`

    /opt/local/bin/dvcmd -u davo -p drc2000 /test/ssh_alarm 1 $USER $ip $port
fi
```

## SSH 접속 ssh-rsa,ssh-dss 에러 문제
- 최신 버전 ssh에서 아래와 같은 에러 메시지 출력하며 접속 안 되는 현상
``` bash
Unable to negotiate with 222.117.116.181 port 822: no matching host key type found. Their offer: ssh-rsa,ssh-dss
```
- 최신 SSH에서 상대적으로 취약한 ssh-rsa, ssh-dss를 기본적으로 지원하지 않아서 벌어지는 문제.
- ssh 명령어 실행 시에 해당 알고리즘으로 시도하도록 옵션 추가 필요.
``` bash
ssh -oHostKeyAlgorithms=+ssh-dss root@192.168.8.109
```

https://askubuntu.com/questions/836048/ssh-returns-no-matching-host-key-type-found-their-offer-ssh-dss
