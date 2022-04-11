# Description
The Linux Command Line - FIfth internet edition 책 시작  
from 25p
# What is shell
## command history
linux terminal은 1000개 정도의 command history를 기억할 수 있다. updown key나 history 커맨드로 확인 가능
## simple command
date -> 날짜 출력
``` bash
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ date
2022. 04. 11. (월) 10:07:04 KST
```
cal -> 달력 출력
``` bash
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ cal
      4월 2022         
일 월 화 수 목 금 토  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30  
```
df -> disc free space
``` bash
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ df
Filesystem     1K-blocks      Used Available Use% Mounted on
udev             8113564         0   8113564   0% /dev
tmpfs            1629480    168472   1461008  11% /run
/dev/sda6       83526192  58003592  21256616  74% /
tmpfs            8147388    124864   8022524   2% /dev/shm
tmpfs               5120         4      5116   1% /run/lock
tmpfs            8147388         0   8147388   0% /sys/fs/cgroup
/dev/sda1         944120    514924    364020  59% /boot
/dev/sdb1      961301832 752859956 159587452  83% /home
cgmfs                100         0       100   0% /run/cgmanager/fs
tmpfs            1629476       100   1629376   1% /run/user/1000
```
free -> display free memory
``` bash
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ free
              total        used        free      shared  buff/cache   available
Mem:       16294780     5841400      303216      295020    10150164     9820524
스왑:    31249404     1057024    30192380
```
## virtual terminal 접속
Ctrl-Alt-F1 에서 Ctrl-Alt-F6
Ctrl-Alt-F7 => Graphical Desktop
# Navigate
Linux Filesystem은 hierarchical directory structure.
Tree like 형식으로 구현됨.

pwd  
-> 현재 directory path 출력

home directory  
-> 처음으로 login 했을 때, 위치하는 디렉터리

ls  
-> 현재 directory의 파일을 listing 함.

cd  
-> change directory 디렉터리 변경 커맨드
- 절대 경로(apsolute pathname) -> 루트 디렉터리부터 목표 파일/디렉터리까지의 경로
- 상대 경로(relative pathname) -> 상대 경로는 작업 디렉터리부터 시작됨.
. -> working directory를 의미함.
.. -> working directory의 parent directory를 의미함.  

이전 directory로 이동
``` bash
cd -
```
특정 유저의 home directory로 이동
``` bash
cd ~user_name
```
### Filename과 관련된 중요 포인트
1. .으로 시작되면 숨김 파일이 되고, ls -a로 전체 파일을 확인해야 표시 가능.
2. case sensitive 함.
3. linux는 file 확장자의 개념이 없다. application program은 파일 확장자에 따라 파일 구분 가능
4. 파일 이름에 embedded spaces and punctuation characters, limit the punctuation characters in the names of files you create to period, dash, and underscore가 사용 가능하지만 spcace는 비추한다.

# Explorer
ls 
-> list directory contents
file 
-> determine file type
less 
-> view file contents
복수 출력 가능
``` bash
jih88@jih88 /usr/sbin $ ls ~ /usr
/home/jih88:
11.4  ML  bin  configs  docker  ent  gww2  ipv6_setting.sh  log  mail  mtk  mtk_main  my_module  proj  ssh  svn_backup  tftproot  tr181  uci_setting  uci_setting.sh  utils  다운로드  문서  바탕화면  비디오  사진  음악

/usr:
aarch64-linux-gnu  arm-linux-gnueabi  arm-linux-gnueabihf  bin  games  include  lib  lib32  libexec  local  sbin  share  src
```
ls -l 
-> detail 출력
``` bash
jih88@jih88 ~ $ ls -l
합계 96
lrwxrwxrwx  1 jih88 jih88    47  8월 30  2021 11.4 -> /home/jih88/proj/SDK_11.4/QCA_SDK_11.4.CSU1_ent
lrwxrwxrwx  1 jih88 jih88    54  8월 10  2021 ML -> /home/jih88/proj/SDK_11.4/QCA_SDK_11.4.CSU1_ent_ML_CFR
drwxrwxr-x  2 jih88 jih88  4096  1월 26 16:09 bin
drwxr-xr-x  3 jih88 jih88  4096  6월  1  2020 configs
drwxrwxr-x  2 jih88 jih88  4096  2월 23 10:20 docker
lrwxrwxrwx  1 jih88 jih88    55  7월 22  2021 ent -> /home/jih88/proj/SDK_11.0/ENT/QCA_SDK_11.2_CS_ent_merge
lrwxrwxrwx  1 jih88 jih88    38  8월 11  2021 gww2 -> /home/jih88/proj/GWW2/QCA_SDK_6.1.0_CS
-rw-rw-r--  1 jih88 jih88  2821  4월  8 09:40 ipv6_setting.sh
drwxrwxr-x  3 jih88 jih88 12288  4월  4 10:13 log
drwxrwxr-x  3 jih88 jih88  4096 10월 20  2020 mail
lrwxrwxrwx  1 jih88 jih88    32  8월  4  2021 mtk -> /home/jih88/proj/mediatek/trunk/
lrwxrwxrwx  1 jih88 jih88    35  3월 11 14:28 mtk_main -> /home/jih88/proj/mediatek/main_repo
drwxr-xr-x 16 jih88 jih88  4096 10월 27 17:12 my_module
drwxrwxr-x 13 jih88 jih88  4096  4월  6 14:44 proj
drwxr-xr-x  2 root  root   4096  2월 16 13:06 ssh
drwxrwxr-x  2 jih88 jih88  4096  4월  5 12:28 svn_backup
lrwxrwxrwx  1 jih88 jih88    18  4월 29  2021 tftproot -> /tmp/symbolic/tftp
lrwxrwxrwx  1 jih88 jih88    62  7월 22  2021 tr181 -> /home/jih88/proj/SDK_11.0/ENT/QCA_SDK_11.2_CS_ent_merge_kt_edu
-rw-rw-r--  1 jih88 jih88    13  4월  7 17:15 uci_setting
-rw-rw-r--  1 jih88 jih88    30  4월  7 17:15 uci_setting.sh
drwxr-xr-x 16 jih88 jih88  4096  3월 15 11:09 utils
drwxr-xr-x  7 jih88 jih88 12288  4월 11 09:53 다운로드
drwxr-xr-x  9 jih88 jih88  4096  4월  5 17:35 문서
drwxr-xr-x  6 jih88 jih88  4096  3월 24 17:53 바탕화면
drwxr-xr-x  3 jih88 jih88  4096  4월 29  2020 비디오
drwxrwxr-x  4 jih88 jih88  4096  2월 14 17:01 사진
drwxrwxr-x  2 jih88 jih88  4096  7월 16  2021 음악
```
## 커맨드 호출 일반적 구조
command -options arguments
ex)
``` bash
jih88@jih88 ~ $ ls -lt /home
합계 32
drwxr-xr-x 68 jih88 jih88    4096  4월 11 10:39 jih88
drwxr-xr-x  9 root  root     4096  7월 15  2021 timeshift
drwxr-xr-x  3 root  root     4096  5월  7  2021 ygjeon
drwxr-x---  6 root  sftpman  4096 11월 30  2020 sftpman
drwx------  2 root  root    16384  4월 29  2020 lost+found
```
## ls 옵션 리스트
-a, --all -> list all files. period로 시작하는 파일 포함.
-A, --almost-all -> .(curent directory), ..(parent directory) 제외하고 list 출력
-d, --directory -> argument directory의 detail을 출력
-F, --classify -> list된 이름에 indicator character를 붙여서 출력. directory의 경우 '/'
-h, --human-readable -> file size가 display될 때, 사람이 읽기 쉬운 형식으로 출력
-l -> display 결과를 long format으로 출력
-r, --reverse -> display 결과를 reverse로 출력
-S -> file size로 sort
-t -> 수정 시간으로 sort

## long format
``` bash
-rw-rw-r-- 1 jih88 jih88   2954  4월  5 11:44 stats_mem.c
```
-rw-rw-r-- -> access right to file(permission)
first charater - type of file(d: directory, -: regular file)
next character - user/group/other permision
1 -> file의 hardlink 숫자.
jih88 -> file 소유자 username
jih88 -> file 소유 groupname
2954 -> 파일 사이즈
4월 5 11:44 -> 파일 마지막 수정 날짜
stats_meme.c -> 파일 이름

## file 명령어
``` bash
jih88@jih88 ~/mtk/build_dir/target-mipsel_24kc_musl-1.1.16/dv_pkg/dvmgmt/statistics $ file stats_mem.c
stats_mem.c: C source, ASCII text
```

## ASCII
- American Standard Code for Information Interchange
- This is a simple encoding scheme that was first used on Teletype machines to map keyboard characters to numbers.
- non-text feature도 포함하고 있다.

## less 명령어
``` bash
jih88@jih88 ~ $ less /etc/passwd
```
Page Up, b -> Scroll back one page
Page Down, space ->  Scroll forward one page
Up arrow -> Scroll up one line
Down arrow -> Scroll down one line
G -> Move to the end of the text file
1G or g -> Move to the beginning of the text file
/characters -> Search forward to the next occurrence of characters
n -> Search for the next occurrence of the previous search
h -> Display help screen
q -> Quit less

more와 less
- less는 more의 대체 프로그램
- more는 scroll forward만 가능하지만, less는 backward, forward 모두 지원

### Linux Filesystem Hierarchy Standard  
standard한 파일 시스템 구조  

'/' -> root directory  
'/bin' -> system booting과 run을 위해 반드시 필요한 binary  
'/boot' -> linux kernel, initial RAM disk 이미지, boot loader 등 부팅에 필요한 파일들  
'/boot/grub/grub.conf' or 'menu.lst' -> bootloader configs  
'/boot/vmlinuz' -> linux kernel  
'/dev' -> device nodes, linux kernel이 관리 하는 device 파일들  
'/etc' -> system-wide configuration files. boot time에서 실행되는 각 system service 파일들  
'/etc/crontab' -> 자동화 작업 파일  
'/etc/fstab' -> storage device 리스트와 각 device의 mounting point  
'/etc/passwd' -> user 계정 리스트  
'/home' -> 각 user별 home directory. 일반 유저는 이 디렉터리만 사용 가능  
'/lib' -> shared library files used by core system, 예를 들면 ext4  
'/media' -> mount points for removable media ex) USB, CD-ROMS  
'/mnt' -> older linux system에서 mount point  
'/opt' -> optional software 설치 포인트, 주로 commercial software  
'/proc' -> 실제 파일시스템이 아님. linux kernel에 의한 virtual filesystem. kernel과의 통신 수단.  
'/root' -> root 계정의 home directory  
'/sbin' -> system binary. super user를 위한 vital system task를 실행.  
'/tmp' -> 다양한 프로그램으로부터 생성된 임시 파일 저장. reboot하면 삭제됨.  
'/usr' -> regular user를 위한 프로그램과 지원 파일들이 포함됨.  
'/usr/bin' -> linux 배포판에 의해 설치된 실행 가능한 binary 프로그램  
'/usr/lib' -> /usr/bin의 프로그램을 위한 shared library  
'/usr/local' ->  distribution 관련 파일은 아니지만 시스템에서 널리 쓰이는 파일 저장 
'/usr/sbin' -> 시스템 관리 프로그램  
'/usr/share' -> /usr/bin에서 사용되는 프로그램의 shared data
'/usr/sahre/doc' -> package에 관련된 documentation  
'/var' -> 변화 가능한 data들을 저장. database, spool files, user mail 등 
'/var/log' -> log files

## Symbolic link
``` bash
lrwxrwxrwx 1 root root 11 2007-08-11 07:34 libc.so.6 -> libc-2.6.so
```
soft link, sym-link라고도 부른다.
file을 다양한 이름으로 참조할 수 있도록 링크 생성

## hard link
hard link 또한 다양한 이름으로 파일을 참조할 수 있도록 함.

# Manipulating Files
cp -> copy files and directory
mv -> move files and directory
mkdir -> make directory
rm - remove files and directory
ln -> create hard and symbolic link
## wildcards
### wildcards
`*` -> matches any characters
`?` -> matches any single charater
`[characters]` -> 어떤 글자든 일치
`[!chracters]` -> member가 아닌 어떤 글자든 일치
`[[:class:]]` -> member 중 어떤 글자든 정의된 class와 일치
### character class
`[:alnum:]` -> alphanumeric 글자와 일치
`[:alpha:]` -> alphabet 글자와 일치
`[:digit:]` -> 숫자와 일치
`[:lower:]` -> 소문자와 일치
`[:upper:]` -> 대문자와 일치
### example
`*` -> All files
`g*` -> All files starts with g
`b*.txt` -> b로 시작하는 txt 파일
`Data???` -> Data로 시작하는 파일 중에 뒤에 정확하게 세글자 더 붙은 파일들
`[abc]*` -> 첫 글자가 a,b,c 중에 하나로 시작하는 파일이
`BACKUP.[0-9][0-9][0-9]` -> BACKUP.으로 시작하고 뒤에 숫자 세 글자가 붙는 파일
`[[:upper:]]*` -> 대문자로 시작하는 파일
`[![:digit:]]*`-> 숫자로 시작하지 않는 파일
`*[[:lower:]123]` -> 소문자 혹은 1,2,3 중에 하나로 끝나는 파일
### Character Ranges
[A-Z][a-z] -> 전통적인 UNIX 표현법. 
## mkdir
crate directory
``` bash
mkdir dir1
```
``` bash
mkdri dir1 dir2 dir3
```
## cp
copy files or directory
### useful options
-a, --archive => copy the files and directories and all of their attributes, including ownership
-i, --interactive => copy하기 전에 copy될 파일이 이미 존재하면 confirm 진행
-r, --recursive => recursively 파일과 directory를 copy
-u, --update => 존재하지 않았거나, 새로 업데이트 된 파일만 copy
-v, --verbose => 정보 message를 출력하면서 copy 진행
### example
cp file1 file2 => file1을 file2로 copy
cp -i file1 file2 => file2가 존재하면 copy하기 전에 물어봄
cp file1 file2 dir1 => file1과 file2를 dir1으로 copy
cp dir1/* dir2 => dir1에 있는 파일들을 dir2로 copy
cp -r dir1 dir2 => dir1과 dir1의 하위 디렉터리에 있는 파일들을 모두 dir2로 copy
## mv
move files or directory
### useful option
-i, --interactive => cp와 유사
-u, --update => cp와 유사
-v, --verbose => cp와 유사
## rm
remove files or directory
### useful option
-i, --interactive => 지우기 전에 confirm
-r, --recursive => 하위 디렉터리를 모두 삭제
-f, --force => confirm 받지 않고 강제로 모두 삭제
-v, --verbose => 삭제 과정 정보를 출력
## ln
create links
create hardlink
``` bash
ln file link
```
create softlink
``` bash
ln -s file link
```
### hard link limitation
file system 외부에서 참조 불가능하다. 같은 disk partition에 없는 파일은 참조 불가능하다.
hardlink는 directory를 참조하는 것이 불가능하다.
### symbolic link
windows shortcut과 비슷하게 동작한다.
symbolic link를 지우면 link만 지워질 뿐 파일은 그대로 있다.
### hardlink
 hardlink를 만들면 같은 data part를 공유하는 추가적인 name part가 생성됨. 따라서 hard link는 파일의 특정 부분을 참조함.
 ### broken link
 link의 목적 파일이 삭제되거나 사라지면 broken link가 됨.
# working with commands
`type` -> command name이 출력되는 방법
`which` -> 실행 가능한 프로그램의 위치
`help` -> help 페이지
`man` -> manual 페이지
`info` -> command info페이지 출력
`whatis` -> one-line mannual 페이지 출력
`alias` -> command의 별명 생성
## command란?
실행 가능한 프로그램
bash shell이 지원하는 커맨드
bash shell script 프로그램
alias
## type
커맨드의 종류를 출력
``` bash
jih88@jih88 ~ $ type type
type is a shell builtin
jih88@jih88 ~ $ type ls
ls 은/는 `ls --color=auto' 의 별칭
jih88@jih88 ~ $ type cp
cp 는/은 /bin/cp
```
## which
커맨드의 위치 출력
``` bash
jih88@jih88 ~ $ which ls
/bin/ls
jih88@jih88 ~ $ which cd
jih88@jih88 ~ $ which node
/usr/local/lib/node/bin/node
```
## help
help 페이지 출력
``` bash
jih88@jih88 ~ $ help cd
cd: cd [-L|[-P [-e]] [-@]] [dir]
    Change the shell working directory.
    
    Change the current directory to DIR.  The default DIR is the value of the
    HOME shell variable.
.
.
.
```
--help로 명령어에서 지원하는 help 출력 가능
``` bash
jih88@jih88 ~ $ mkdir --help
사용법: mkdir [옵션]... 디렉터리...
Create the DIRECTORY(ies), if they do not already exist.

Mandatory arguments to long options are mandatory for short options too.
  -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask
  -p, --parents     no error if existing, make parent directories as needed
  -v, --verbose     print a message for each created directory
.
.
.
```
## man
프로그램의 manual page 출력
``` bash
man ls
```
## apropos
man page search 기능
``` bash
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ apropos ftp
apt-ftparchive (1)   - Utility to generate index files
conchftp (1)         - Conch command-line SFTP client
filezilla (1)        - FTP client
ftp (1)              - Internet file transfer program
fzputtygen (1)       - SFTP private key converter of FileZilla
fzsftp (1)           - SFTP connection handler of FileZilla
...
```
## whatis
한 줄 자리 man page 출력
``` bash
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ whatis ls
ls (1)               - list directory contents
```
## info
man page의 대안으로서 만들어진 manual page
``` bash
info ls
```
## alias
한 번에 여러 커맨드 입력
``` bash
command1; command2; command3...
```
ex)
``` bash
cd /usr; ls; cd -
```
alias 사용법
``` bash
alias name='string'
```
ex)
``` bash
alias foo='cd /usr; ls; cd -'
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ foo
aarch64-linux-gnu  arm-linux-gnueabi  arm-linux-gnueabihf  bin  games  include  lib  lib32  libexec  local  sbin  share  src
/home/jih88/proj/mediatek/ntv4ov6
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ type foo
foo 은/는 'cd /usr; ls; cd -' 의 별칭
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ unalias foo
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ type foo
bash: type: foo: 발견되지 않음
```
alias는 shell session이 닫히면 사라진다.
# Redirection
I/O Redirection
I/O => Input/Output, command의 output을 file이나 다른 command의 input으로 redirect 가능
`cat` => concatenate files
`sort` => sort lines of text
`uniq` => 반복된 라인을 보고 또는 생략
`grep` => pattern에 맞는 line을 print
`wc` => 파일로 print neline, word, and byte counts
`head` => 파일 윗 부분의 output
`tail` => 파일 뒷 부분의 output
`tee` => standard input으로부터 값을 읽어서, standard output이나 파일로 출력
## standard input, standard output, standard error
program의 output은 standard output/error를 통하여 화면으로 print
keyboard 등의 입력 장비로 입력된 값은 standard input으로 입력받아 프로그램에 입력
## I/O Redirection
Standard Output이 향하는 곳을 재정의할 수 있음.
`>` -> redirection operation, standard output의 목적지를 재정의
-> destination file은 항상 rewritten된다.  
ex)
``` bash
ls -l /usr/bin > ls-output.txt
```
에러메시지가 파일로 저장되지 않는 이유
``` bash
jih88@jih88 ~ $ ls -l /bin/usr > ls-output.txt
ls: '/bin/usr'에 접근할 수 없습니다: 그런 파일이나 디렉터리가 없습니다
```
=> standard error는 standard output으로 전달되지 않는다.
`>>` -> redirect할 때, file에 rewrite하지 않고 append한다.
## Redirecting Standard Error
``` bash
ls -l /bin/usr 2> ls-error.txt
```
## Redirectng Standard Output/Error to One File
``` bash
ls -l /bin/usr > ls-output.txt 2>&1
```
최근 bash에서는 하나의 notation으로 standard output과 standard error를 동시에 출력하도록 구현
``` bash
ls -l /bin/usr &> ls-output.txt
```
append도 가능
``` bash
ls -l /bin/usr &>> ls-output.txt
```
## disposal output
`/dev/null` 로 redirect
bit bucket이라고도 불림
``` bash
ls -al /usr/sbin > /dev/null
```
## Redirecting Standard Input
## cat - Concatenate Files
raad one or more files and copy them to standard output
``` bash
cat [file ...]
```
