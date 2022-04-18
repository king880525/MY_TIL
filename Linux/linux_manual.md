# 개요
linux 사용법 공부하며 정리할 부분 정리한 문서
# 서비스와 소켓
서비스=데몬=서버 프로세스
서비스 - 평상 시에도 늘 가동하는 서버 프로세스
소켓 - 필요할 때만 작동하는 서버 프로세스
-> 서비스와 소켓을 systemd에서 서비스 매니저 프로그램으로 작동시키거나 관리
## 서비스
- 시스템과 독자적으로 구동 및 제공되는 프로세스
- 실행 및 종료 -> `systemctl start/stop/restart 서비스 이름`
- 서비스의 실행 스크립트 파일 위치 -> `/usr/lib/systemd/system/`에 `서비스이름.service`
- 터미널에서 `systemctl list-unit-files` 명령을 통해 사용/사용 안함 여부 확인 가능
## 소켓
- 외부에서 특정 서비스 요구시 systemd가 구동
- 서비스에 비해 구동 시간이 더 걸린다. (새로 서비스 구동하는 데 시간 걸림)
- 소켓 관련 스크립트 파일은 `/usr/lib/systemd/system/`디렉터리에 `소켓이름.socket`으로 존재
# 응급 복구
1. GRUB 메뉴에서 `E`입력
2. `linux ($root)/boot/vm/linuz...`에 커서를 가져다 놓고 end로 행 끝으로 이동하여 뒤쪽의 `rhgb quiet`를 삭제하고 제일 뒤에 `init=/bin/sh`를 입력
3. `Ctrl+X`를 입력하여 부팅
4. `whoami`를 입력하여 현재 사용자가 root인지 확인
5. `mount -o remount,rw /` 명령을 입력해서 `/`파티션을 읽기/쓰기 모드로 다시 마운트
6. `passwd root`를 이용하여 root 암호 변경

# GRUB 부트로더
## GRUB의 특징
- 부트 정보를 사용자가 임의로 변경하여 부팅 가능
- 여러가지 운영체제로 멀티 부팅 가능
- 대화형 설정을 제공 -> 커널 경로와 파일 이름만 알면 부팅 가능
## GRUB2의 장점
- 쉘 스크립트 지원
- 동적 모듈 로드 가능 -> 동적모듈은 /boot/grub2/i386-pc/ 디렉터리에 mod 파일로 존재.
- 그래픽 부트 메뉴 지원 -> 부트 스플래시 성능이 개선
- ISO 이미지를 이용해서 바로 부팅 가능
## GRUB2
- 설정 파일: `/boot/grub2/grub.cfg`
- 링크파일: `/etc/grub2.cfg`
- 설정 내용 적용: `/etc/default/grub` 파일과 `/etc/grub.d/` 디렉터리 파일 수정 후 `grub2-mkconfig` 명령 실행.
## /etc/default/grub 파일 설정
``` bash
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="$(sed's.release.*$g'/etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX="crashkernel=auto resume=UUID=장치코드고유번호 rhgb quiet"
GRUB_DISABLE_RECOVERY="true"
GRUB_ENABLE_BLSCFG=true
```
1행 -> 청음 화면이 나오고 자동으로 부팅되는 시간(초단위, -1이면 사용자의 엔트리 선택 대기)
2행 -> 초기 부팅 화면의 각 엔트리 앞에 붙을 배포판 이름 추출.
3행 -> saved(이전에 선택한 엔트리 기본 선택), 0번이면 첫번째 엔트리
4행 -> 서브 메뉴 사용 여부 결정, 기본값 true면 서브 메뉴 사용 안 함.
5행 -> GRUB가 나올 장치 설정. 기본값을 console로 해 두면 모니터로 출력. serial, gfxterm 등 설정 가능.
6행 -> 부팅 시 커널에 전달할 파라미터 지정. init=/bin/bash와 같이 설정 가능
7행 -> true로 설정하면 메뉴 엔트리에서 복구와 관련된 것을 비활성화
8행 -> BLSCFG는 Bootloader Spec For congiuration의 약자. 변경할 필요 없음.
## GRUB Booting Timeout 변경
1. `vi /etc/default/grub` 실행
2. `GRUB_TIMEOUT=20`값을 원하는 Timeout 파라미터로 변경
3. 변경 내용 적용을 위해 `grub2-mkconfig -o /boot/grub2/grub.cfg` 명령을 입력
## GRUB 비밀번호 변경 차단
1. vim으로 `/etc/grub.d/00_header`파일을 연다.
2. 제일 아래에 grub 편집 가능한 사용자 지정을 위한 코드 입력
```
cat << EOF
set supserusers="thisislinux"
password thisislinux 1234
EOF
```
3. 변경 내용 적용을 위해 `grub2-mkconfig -o /boot/grub2/grub.cfg` 명령을 입력
# 커널 컴파일
## 모듈(module)
- 커널 외에 별도로 보관했다가 필요할 때 로드해서 사용하는 코드
## 커널 컴파일 순서
1. 현 커널 버전 확인(#uname -r)
2. 커널 소스 다운로드
3. 커널 소스 압축풀기
4. 커널 설정 초기화 - `#make mrproper`
5. 커널 환경 설정 - `#make xconfig`
6. .config 편집 및 이전 정보 삭제 - .config 파일 편집, `make clean`
7. 커널 컴파일 및 설치 - `make` `make modules_install` `make install` `ls -l /boot`
8. 부트로더 확인 - `cat /etc/grub2/grub.cfg`
   
# CentOS 테마 패키지
1. 패키지 설치
``` bash
su -c 'dnf -y install gnome-tweak-tool'
```
2. gnome-tweaks 실행하여 테마 꾸미기
``` bash
gnome-tweaks
```
# GRUB 화면 꾸미기
1. 꾸미고자 하는 이미지(png)를 `/boot/grub2/`로 옮긴다.
2. `su -c 'vi /etc/default/grub'`를 입력하여 grub 설정파일을 연다.
3. 아래와 같이 BACKGROUND 파라미터를 추가하고, GRUB_TERMINAL_OUTPUT 행 앞에 #으로 주석처리한다.
``` bash
#GRUB_TERMINAL_OUTPUT="console"
GURB_BACKGROUND="/boot/grub2/wall.png
```
4. `su -c 'grub2-mkconfig -o /boot/grub2/grub.cfg'` 명령을 입력하여 grub2 파일을 적용한다.
# x윈도우 어플리케이션
## 노틸러스
- 파일 브라우저
## 브라세로
- CD/DVD ISO 파일 제작 프로그램