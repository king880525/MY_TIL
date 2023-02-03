## bash란
Bash 는 Bourne Again Shell의 축약어이다. 이것은 원래의 본쉘과 호환이 가능하며 명령 라인 편집과 같은 몇 가지 점에서 기능이 향상되었다. 또한 Bash쉘은 리눅스 쉘이며 리눅스에서 가장 널리 사용되는 쉘이다.
## 설정 파일들
bash는 다섯개의 공통된 설정 파일들을 가지고 있다. 
모든 리눅스 배포본에 존재하지는 않지만 이 파일들을 만드는 것은 어렵지 않다.
``` bash
/etc/profile
/etc/bashrc
~/.bash_profile
~/.bashrc
~/.bash_logout
```
이 파일들은 전역적인 것과 지역적인 것의 두 개 그룹으로 나누어질 수 있다. 
bash를 사용하는 모든 사용자에게 영향을 주는 설정 내용을 담고 있는 파일들은 전역적이다. 
일반적으로 전역적인 파일은 /etc 디렉토리에 위치한다. 
지역적인 파일은 사용자 개개인을 위한 설정내용을 담고 있어서 그 파일을 사용하는 특정 사용자에게만 영향을 끼치는 파일들을 뜻한다. 
이들은 대개 사용자의 홈 디렉토리에서 찾아 볼 수 있는 숨김파일이다. (숨김 파일의 경우 .으로 시작한다. ex] ~/.bashrc)
## 전역 설정 파일
/etc/profile
/etc/profile은 환경변수와 bash가 수행될 때 실행되는 프로그램을 제어하는 전역적인 시스템 설정과 관련된 파일이다.
/etc/bashrc
/etc/bashrc는 별칭(alias)과 bash가 수행될 때 실행되는 함수를 제어하는 전역적인 시스템 설정과 관련된 파일이다. 별칭은 물론 불려질때 실행되는 짤막한 코드도 포함하고 있다. 때때로 /etc/bashrc는 생략되기도 하며 그 내용은 /etc/profile에 함께 포함되기도 한다.
/etc/bash.bash_logout
~/.bash_logout 은 사용자가 로그 아웃하기 바로 직전에 실행하는 프로그램에 관한 bash의 전역적인 시스템 설정과 관련된 파일이다.
## 지역 설정 파일
~/.bash_profile
~/.bash_profile은 환경변수와 bash가 수행될 때 실행되는 프로그램을 제어하는 지역적인 시스템설정과 관련된 파일이다. 이들 환경 변수들은 오직 그 사용자에게많 한정되며, 그 이외의 다른사람에게는 영향을 미치지 않는다. 이 파일은 전역적인 설정파일인 /etc/profile이 수행된다음 바로 수행된다.
~/.bashrc
~/.bashrc는 별칭(alias)과 bash가 수행될 때 실행되는 함수를 제어하는 지역적인 시스템 설정과 관련된 파일이다. 이들 별칭과 함수들은 오직 그 사용자에게만 한정되며, 그 이외의 다른사람에게는 영향을 미치지 않는다. 이 파일은 전역적인 설정파일인 /etc/bashrc이 수행된 다음 바로 수행된다.
~/.bash_logout
~/.bash_logout 은 사용자가 로그 아웃하기 바로 직전에 실행하는 프로그램에 관한 bash의 지역적인 시스템 설정과 관련된 파일이다. 이들 프로그램은 오직 그 프로그램을 실행하는 사용자에게만 영향을 끼치지 다른사람에게는 아무런 영향을 주지 않는다.
ex) /etc/bash.bash_logout
``` bash
#!/bin/sh
if [ -n "$SSH_CONNECTION" ]; then
    ip=`echo $SSH_CONNECTION | cut -d " " -f 1`
    port=`echo $SSH_CONNECTION | cut -d " " -f 2`

    /opt/local/bin/dvcmd -u davo -p drc2000 /test/ssh_alarm 2 $USER $ip $port
fi
```

# 특수 매개변수
`$$` - 현재 스크립트의 PID
`$?` - 최근에 실행된 명령어, 함수, 스크립트 자식의 종료 상태
`$!` - 최근에 실행한 백그라운드(비동기) 명령의 PID
`$-` - 현재 옵션 플래그
`$_` - 지난 명령의 마지막 인자로 설정된 특수 변수

`-a` -> &&, ex) `if [ candy -a strawberry ];`

# 링크
https://blog.gaerae.com/2015/01/bash-hello-world.html