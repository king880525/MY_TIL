# 0. Description
The Linux Command Line - FIfth internet edition 책 시작  
from 25p
# 1. What is shell
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
# 2. Navigate
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

# 3. Explorer
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

# 4. Manipulating Files
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
# 5. working with commands
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
# 6. Redirection
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
paging 없이 file 출력 가능.
ex)
``` bash
cat movie.mpeg.0* > movie.mpeg
```
- filename argument 없이 cat을 사용하면, standard input을 copy하여 standard output으로 copy하는 동작을 한다.
- redirection을 이용해 standard input을 다른 파일로 copy하는 동작도 가능하다.
``` bash
cat > lazydog.txt
```
- 반대로 file에서 standard output으로 출력하는 방법도 가능하다.
``` bash
cat < lazydog.txt
```
## pipeline
standard input에서 data를 읽어 standard output으로 data 전송
command의 statndard output을 다른 command의 standard input으로 활용 가능하다
ex)
``` bash
ls -l /usr/bin | less
```
`>`와 `|`의 다른점
`>`은 command에 standard input을 입력할 수 없으나, `|`는 가능하다.
``` bash
ls > less
```
위와 같이 사용하면 ls의 결과물이 less 명령어 파일에 입력됨으로서 less 명령어가 파괴된다.
redirection 사용에는 주의가 필요하다.
### Filters
pipeline은 sort와 같은 명령어를 이용하여 주로 필터 용도로 사용됨.
ex)
``` bash
ls /bin /usr/bin | sort | less
```
### uniq
duplicate된 line을 제거
``` bash
ls /bin /usr/bin | sort | uniq | less
```
dupicated된 line만 출력
``` bash
ls /bin /usr/bin | sort | uniq -d | less
```
### wc
line의 개수, 단어의 개수, file의 총 byte수 등을 출력
``` bash
jih88@jih88 ~ $ wc ls-output.txt
  2986  28049 204019 ls-output.txt
```
겹치지 않는 item의 개수 출력
``` bash
ls /bin /usr/bin | sort | uniq | wc -l
```
### grep
text 패턴을 찾아내는 프로그램
``` bash
grep pattern [file ...]
```
ex)
``` bash
jih88@jih88 ~ $ ls /bin /usr/bin | sort | uniq | grep zip
bunzip2
bzip2
bzip2recover
funzip
gpg-zip
gunzip
gzip
mzip
p7zip
preunzip
prezip
prezip-bin
unzip
unzipsfx
zip
zipcloak
zipdetails
zipgrep
zipinfo
zipnote
zipsplit
```
`-i` -> ignore case
`-v` -> line과 match되지 않는 패턴 출력
## head/tail
head -> first line of file 출력
tail -> last line of file 출력
``` bash
jih88@jih88 ~ $ head -n 5 ls-output.txt 
합계 1094764
-rwxr-xr-x 1 root root            96  3월 18 22:21 2to3-2.7
-rwxr-xr-x 1 root root            96  1월 27  2021 2to3-3.5
-rwxr-xr-x 1 root root         10104  4월 23  2016 411toppm
-rwxr-xr-x 1 root root            40  2월  6  2018 7zr
jih88@jih88 ~ $ tail -n 5 ls-output.txt 
-rwxr-xr-x 2 root root        178312 11월 27  2020 zipinfo
-rwxr-xr-x 1 root root         89488  4월 22  2017 zipnote
-rwxr-xr-x 1 root root         93584  4월 22  2017 zipsplit
-rwxr-xr-x 1 root root         26624  2월 26  2018 zjsdecode
-rwxr-xr-x 1 root root         10336  7월 28  2021 zlib-flate
```
명령어와의 조합
``` bash
jih88@jih88 ~ $ ls /usr/bin/ | tail -n 5
zipinfo
zipnote
zipsplit
zjsdecode
zlib-flate
```
변경되는 파일을 실시간으로 출력
``` bash
tail -f /var/log/syslog
```
## tee
standard input으로부터 data를 읽어들임과 동시에 standard output과 파일로 동시에 출력
ex)
``` bash
jih88@jih88 ~ $ ls /usr/bin | tee ls.txt | grep zip
funzip
gpg-zip
mzip
p7zip
preunzip
prezip
prezip-bin
unzip
unzipsfx
zip
zipcloak
zipdetails
zipgrep
zipinfo
zipnote
zipsplit
```
# 7. echo
echo - text argument를 standard output으로 출력
``` bash
jih88@jih88 ~ $ echo this is a test
this is a test
```
``` bash
jih88@jih88 ~ $ echo *
11.4 ML bin configs docker ent gww2 ipv6_setting.sh lazy_dog.txt log ls-output.txt ls.txt mail mtk mtk_main my_module proj ssh svn_backup tftproot tr181 uci_setting uci_setting.sh utils 다운로드 문서 바탕화면 비디오 사진 음악
```
## Expansion
### pathname expansion
wildcard의 동작 매커니즘을 pathname expansion이라고 정의할 수 있다.
``` bash
jih88@jih88 ~ $ echo ipv*
ipv6_setting.sh
jih88@jih88 ~ $ echo *s
configs utils
jih88@jih88 ~ $ echo [[:upper:]]*
ML
jih88@jih88 ~ $ echo /usr/*/share
/usr/local/share
```
ls의 옵션들은 내부적으로 echo로 구현되어 있다.
``` bash
echo .[!.]*
ls -A
```
### Tilde Expansion
tilde character (~)는 home directory를 의미함
``` bash
echo ~
echo ~jih88
```
### Arithmetic Expansion
`$((expression))` 과 같은 형식으로 사용
``` bash
jih88@jih88 ~ $ echo $((2+2))
4
jih88@jih88 ~ $ echo $((3-2))
1
jih88@jih88 ~ $ echo $((3*3))
9
jih88@jih88 ~ $ echo $((4/2))
2
jih88@jih88 ~ $ echo $((3%2))
1
jih88@jih88 ~ $ echo $((4**2))
16
```
``` bash
jih88@jih88 ~ $ echo $(($((5**2))*3))
75
```
문자와 조합한 표현
``` bash
jih88@jih88 ~ $ echo Five divide by two equals $((5/2))
Five divide by two equals 2
jih88@jih88 ~ $ echo with $((5%2)) left over.
with 1 left over.
```
### Brace Expansion
pattern을 포함한 brace를 이용한 multiple text string 생성 가능
``` bash
jih88@jih88 ~ $ echo Front-{A,B,C}-Back
Front-A-Back Front-B-Back Front-C-Back
jih88@jih88 ~ $ echo Number_{1..5}
Number_1 Number_2 Number_3 Number_4 Number_5
jih88@jih88 ~ $ echo {01..15}
01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
jih88@jih88 ~ $ echo {001..15}
001 002 003 004 005 006 007 008 009 010 011 012 013 014 015
jih88@jih88 ~ $ echo {Z..A}
Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
jih88@jih88 ~ $ echo a{A{1,2},B{3,4}}b
aA1b aA2b aB3b aB4b
```
아래와 같이 활용 가능
``` bash
jih88@jih88 ~/photos $ mkdir {2007..2009}-{01..12}
jih88@jih88 ~/photos $ ls
2007-01  2007-03  2007-05  2007-07  2007-09  2007-11  2008-01  2008-03  2008-05  2008-07  2008-09  2008-11  2009-01  2009-03  2009-05  2009-07  2009-09  2009-11
2007-02  2007-04  2007-06  2007-08  2007-10  2007-12  2008-02  2008-04  2008-06  2008-08  2008-10  2008-12  2009-02  2009-04  2009-06  2009-08  2009-10  2009-12
```
### Parameter Expansion
shell에 변수를 지정하여 저장할 수 있다.
shell script에서 유용하게 활용된다.
``` bash
jih88@jih88 ~ $ echo $USER
jih88
jih88@jih88 ~ $ echo $SUSER
```
### Command Substitution
command의 output을 expansion으로 사용 가능
``` bash
jih88@jih88 ~ $ echo $(ls)
11.4 ML bin configs docker ent gww2 ipv6_setting.sh lazy_dog.txt log ls-output.txt ls.txt mail mtk mtk_main my_module proj ssh svn_backup tftproot tr181 uci_setting uci_setting.sh utils 다운로드 문서 바탕화면 비디오 사진 음악
jih88@jih88 ~ $ ls -l $(which cp)
-rwxr-xr-x 1 root root 141528  1월 18  2018 /bin/cp
```
older system에서는 backquote를 사용했고 지금도 사용 가능
``` bash
jih88@jih88 ~ $ ls -l `which cp`
-rwxr-xr-x 1 root root 141528  1월 18  2018 /bin/cp
```
## Quoting
expansion으로 오인하여 일반 strng이 잘못 출력되는 이슈 발생
``` bash
jih88@jih88 ~ $ echo this is a            test
this is a test
jih88@jih88 ~ $ echo The total is $100.00
The total is 00.00
```
quoting으로 일반 string을 정상 출력 가능
### Double Quotes
- $, \(backslash), `(backquotes)를 제외하면 double quates 안에 들어가면 일반 string으로 인식됨.
- word-splitting, pathname expansion, tilde expansion, brace exapansion은 무시되고, parameter expansion, arithmetic expansion, command substitution은 여전히 동작함.
``` bash
jih88@jih88 ~ $ touch "two words.txt"
jih88@jih88 ~ $ ls -l two words.txt
ls: 'two'에 접근할 수 없습니다: 그런 파일이나 디렉터리가 없습니다
ls: 'words.txt'에 접근할 수 없습니다: 그런 파일이나 디렉터리가 없습니다
jih88@jih88 ~ $ ls -l "two words.txt"
-rw-rw-r-- 1 jih88 jih88 0  4월 12 12:24 'two words.txt'
```
``` bash
jih88@jih88 ~ $ echo "$USER $((2+2)) $(cal)"
jih88 4       4월 2022         
일 월 화 수 목 금 토  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30 
```
``` bash
jih88@jih88 ~ $ echo this is a             test
this is a test
jih88@jih88 ~ $ echo "this is a           test"
this is a           test
```
word-splitting mechanism에서는 neline이 delimitter로 고려되지 않는다.
double quote를 적용하면 delimiter로 적용된다.
``` bash
jih88@jih88 ~ $ echo $(cal)
4월 2022 일 월 화 수 목 금 토 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
jih88@jih88 ~ $ echo "$(cal)"
      4월 2022         
일 월 화 수 목 금 토  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30  
```
### Single Quotes
single quotes는 expansion을 허용하지 않는다.
``` bash
jih88@jih88 ~ $ echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER 
text /home/jih88/lazy_dog.txt /home/jih88/ls-output.txt /home/jih88/ls.txt /home/jih88/two words.txt a b foo 4 jih88
jih88@jih88 ~ $ echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"
text ~/*.txt {a,b} foo 4 jih88
jih88@jih88 ~ $ echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'
text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER
```
### Escaping Characters
single character만 quoting하고 싶을 때 사용
``` bash
jih88@jih88 ~ $ echo "The balance for user $USER is: \$5.00"
The balance for user jih88 is: $5.00
```
### Backslash Escape Sequences
\(backslash)를 사용하여 control code를 사용할 수 있다.
`\a` => 비프음
`\b` => backspace
`\n` => newline
`\r` => carrage return
`\t` => tab
echo에는 \n이 추가되며, 이가 제거된 echo를 출력하려면
`echo -e`와 같이 `-e`를 추가하여 제거 가능
# 8. Advanced Keyboard Command
## Command Line Editing
### Cursor Movement
Ctrl+A => 라인 맨 앞으로 이동
Ctrl+E => 라인 맨 뒤로 이동
Ctrl+F => 한글자씩 앞으로 이동
Ctrl+B => 한글자씩 뒤로 이동
Alt+F => 한단어씩 앞으로 이동
Alt+B => 한단어씩 뒤로 이동
Ctrl+l => screen을 clear함. clear 커맨드와 유사
### Modifying Text
Ctrl+D => 커서 위치에 있는 글자 제거된
Ctrl+T => 커서 위치에 있는 글자와 그 앞의 글자 치환
Alt+T => 커서 위치에 있는 단어와 그 앞의 단어 치환
Alt+l => 커서 위치부터 단어 끝까지의 알파벳을 lower case로 변경
Alt+u => 커서 위치부터 단어 끝까지의 알파벳을 upper case로 변경
### Cutting and Pasting(Killing and Yanking)
Ctrl+k => 커서부터 라인 끝까지 delete
Ctrl+u => 커서부터 라인 시작까지 delete
Alt+d => 커서부터 현재 단어 끝까지 delete
Alt+backspace => 커서부터 현재 단어 시작점까지 delete
Ctrl+y => delete한 text 붙여넣기
## Completion
한글자만 입력한 상태에서 tab하면 자동으로 채워준다.
### completion 관련 command
Alt+? => 가능한 커맨드 디스플레이
Alt+* => 가능한 커맨드 입력
## Using History
home directory의 .bash_history에 명령어 내역을 저장함.
`history` => 명령어 호출 내역 확인하는 명령어
`!번호` => 해당 커맨드 index에 해당하는 명령어 실행
``` bash
jih88@jih88 ~ $ history | tail
 2115  ls /bin /usr/bin | sort | uniq | grep -v zip
 2116  history
 2117  history | tail
 2118  ls /bin /usr/bin | sort | uniq | grep -v zip
 2119  history
 2120  ls -al | grep zip
 2121  ls
 2122  ls -al | grep ent
 2123  history
 2124  history | tail
jih88@jih88 ~ $ !2122
ls -al | grep ent
lrwxrwxrwx  1 jih88 jih88     47  8월 30  2021 11.4 -> /home/jih88/proj/SDK_11.4/QCA_SDK_11.4.CSU1_ent
lrwxrwxrwx  1 jih88 jih88     54  8월 10  2021 ML -> /home/jih88/proj/SDK_11.4/QCA_SDK_11.4.CSU1_ent_ML_CFR
lrwxrwxrwx  1 jih88 jih88     55  7월 22  2021 ent -> /home/jih88/proj/SDK_11.0/ENT/QCA_SDK_11.2_CS_ent_merge
lrwxrwxrwx  1 jih88 jih88     62  7월 22  2021 tr181 -> /home/jih88/proj/SDK_11.0/ENT/QCA_SDK_11.2_CS_ent_merge_kt_edu
```
`Ctrl+r` => history search
history search하는 도중에 선택한 커맨드를 `Enter` 혹은 `Ctrl+j` 시에 커맨드 입력
history search하는 도중에 선택한 커맨드를 `Ctrl+g` 혹은 `Ctrl+c` 시에 커맨드 입력취소
### history command
`Ctrl+p` => previous(이전 히스토리로 이동)
`Ctrl+n` => next
`Alt+<` => beginning of history로 이동
`Alt+>` => end of history로 이동
`Ctrl+r`=> reverse incremental search
`Alt+p` => reverse search
`Alt+n` => Forward search
`Ctrl+o` => 현재 history item을 실행하고 다음 item으로 이동
### history expansion
`!!` => repeat last command
`!string` => history 중에 string으로 시작하는 command를 실행
`!?string` => history 중에 string을 포함하는 command 실행
### script
script [file]
shell에 출력된 모든 로그를 file에 저장
# 9. Permission
Unix, Linux는 Multitasking, Multi-user system
`id` -> display user identify
`chmod` -> change file's mode
`umask` -> set default file permission
`su` -> run a shell as super user
`sudo` -> execute a command as anoter user
`chown` -> change file's owner
`chgrp` -> change file's group
`passwd` -> change a user's password
## owners, group members, and others
regular user는 system file을 읽을 권한이 없다.
id 커맨드를 통해 user의 identify 정보 확인 가능
``` bash
jih88@jih88 ~/proj/mediatek/ntv4ov6 $ id
uid=1000(jih88) gid=1000(jih88) 그룹들=1000(jih88),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),130(sambashare)
```
user account 정보 파일 -> `/etc/passwd`  
group account 정보 파일 -> `/etc/group`  
user/group password 정보 파일 -> `/etc/shadow`  
superuser는 uid(0)
## Reading, Writing, Executing
### File Type
`-` -> 일반 파일
`d` -> 디렉터리
`l` -> 심볼릭 링크
`c` -> character special file. device that handles data as a stream
`b` -> block special file. device that handles data in blocks
### permission attribute
`r` -> read and open
`w` -> write and append, and delete
`x` -> treat as a program, execute
### chmod
permision 변경 가능
``` bash
chmod 600 foo.txt
```
### chmod symbolic notation
`u` -> user
`g` -> group
`o` -> others
`a` -> all
### umask
파일을 생성하면 permission이 644로 표기됨.
``` bash
jih88@jih88 ~ $ ls -al foo.txt 
-rw-rw-r-- 1 jih88 jih88 5  4월 12 15:53 foo.txt
jih88@jih88 ~ $ umask
0002
```
original file mode가 666
umask가 002
mask 적용하면 644
`umask [permision]` 명령어로 umask 변경 가능.
### special permission
- setuid bit(octal 4000)
root 사용자의 파일을 일반 사용자가 접근 가능.
- setgid bit(octal 2000)
setuid group 버전
- sticky bit(octal 1000)
sticky bit가 설정되면 디렉터리 소유자나 파일 소유자, 슈퍼 유저가 아닌 사용자들은 파일 삭제, 이름 변경 불가능
## change identities
권한 획득 방법
1. 권한 있는 사용자로 login
2. su 커맨드 사용
3. sudo 커맨드 사용
### su
임시 유저나 임시 그룹으로 shell 사용  
superuser로 shell 실행
``` bash
su -
```
superuser로 command 실행
``` bash
su -c 'command'
```
### sudo
다른 유저의 권한으로 command 실행
sudo로 어떤 권한이 보장되는지 아래 커맨드로 확인 가능
``` bash
sudo -l
```
### chown
파일의 소유자와 그룹을 변경
``` bash
chown bob:users test.sh
```
### chgrp
파일의 그룹 소유자를 변경. chown과 유사
## changing password
`passwd` 명령어를 이용하여 user의 password 변경 가능
### futher reading
adduser, useradd, groupadd로 user 및 group 생성 가능. 
# 10. Processes
`ps` -> 현재 process에 대한 snapshot 출력
`top` -> task를 출력
`jobs` -> 활성화된 job 표시
`bg` -> job을 background로 위치
`fg` -> job을 foreground로 위치
`kill` -> process에 signal 전송
`killall` -> 이름으로 process kill
`shutdown` -> system을 shutdown하거나 reboot
## process 동작 방식
kernel init 단계에서 init process 실행  
/etc에 있는 script를 init process에서 실행 
/etc에 있는 script는 daemon program(background에서 동작, user interface 없음.)
program이 다른 program을 실행할 때, 실행하는 process를 parent process, 실행되는 process를 child process라고 함.
process ID(PID) - 각 process에 부여되는 ID
process마다 memory가 assign되어 있고, owner가 있고, user id가 있음.
## Viewing Processes
ps 명령어는 current terminal session과 연관된 process만 표시  
추가적인 정보를 위해서는 option 추가 필요
``` bash
jih88@jih88 ~ $ ps
  PID TTY          TIME CMD
24904 pts/0    00:00:00 bash
24946 pts/0    00:00:00 ps
```
TTY -> short for "teletype", controlling terminal for the process
TIME -> ammount of CPU time consumed by the process
x 옵션 => 어떤 프로세스가 어떤 터미널에 의해 control되는지 모든 리스트 출력. 우리가 소유한 process만 출력.
``` bash
jih88@jih88 ~ $ ps x
  PID TTY      STAT   TIME COMMAND
  405 pts/4    Ss+    0:02 bash
 3868 ?        Sl     7:19 gksudo remmina
 3873 ?        Ss     0:00 /lib/systemd/systemd --user
...
```
STAT -> short for "state", process의 현재 상태 출력
#### process state
`R` -> Running, running or ready to run
`S` -> Sleeping, waiting for a event
`D` -> Uninterruptible sleep, wait for I/O
`T` -> Stopped
`Z` -> Zombie process, not cleaned child process
`<` -> high-priority process, 좀 더 많은 CPU 타임을 할애받음.
`N` -> low-priority process, 모든 higher priority process가 끝나야 CPU 타임을 할애받음.

ps aux -> 자주 사용되는 option
``` bash
jih88@jih88 ~ $ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0 226432  7124 ?        Ss    3월21   0:39 /sbin/init splash
root         2  0.0  0.0      0     0 ?        S     3월21   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<    3월21   0:00 [kworker/0:0H]
```
#### BSD Stype PS Column Header
`USER` -> User ID
`%CPU` -> CPU Usage in Percent
`%MEM` -> Memory Usage in Percent
`VSZ` -> Virtual Memory Size
`RSS` -> Resident Set Size. process가 사용하고 있는 Physical memory(RAM)
`START` -> Process가 시작된 시간. 24시간이 넘어가면 date가 사용됨.

### Viewing process dynamically with top
top 명령어는 machine's activity를 dynamic하게 출력  
top program은 every three seconds마다 지속적으로 update  
top 프로그램은 두 가지 part로 구성. system summary, process table list  
``` bash
jih88@jih88 ~ $ top

top - 09:39:19 up 23 days, 39 min,  1 user,  load average: 0.30, 0.48, 0.61
Tasks: 309 total,   1 running, 252 sleeping,   0 stopped,   0 zombie
%Cpu(s):  5.2 us,  1.1 sy,  0.0 ni, 93.2 id,  0.4 wa,  0.0 hi,  0.1 si,  0.0 st
KiB Mem : 16294780 total,  2057976 free,  5171524 used,  9065280 buff/cache
KiB Swap: 31249404 total, 30237436 free,  1011968 used. 10517372 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                                                                                                                                   
 1839 root      20   0 1126568 195924  71696 S  12.5  1.2   1905:39 Xorg                                                                                                                                                                      
27122 jih88     20   0   43380   4036   3192 R  12.5  0.0   0:00.03 top                                                                                                                                                                       
 3980 jih88     20   0  359604   8652   3224 S   6.2  0.1  51:52.56 ibus-daemon   
 ...
 ```
 #### top information field
`top` - 프로그램 이름
`09:39:19` - 현재 시간 
`up 23 days, 39 min` - uptime
`1 user` - login한 user가 1명  
`load average` - run을 기다리고 있는 preocess 의 개수. 처음은 마짐막 60초, 그 다음은 이전 5분, 마지막으로 이전 15분. 1.0보다 낮은 값은 mahchine이 busy하다는 것을 의미.
`Tasks:` -  process 개수와 process 상태 출력
`%Cpu(s):` - cpu 사용 정보 출력  
`5.2 us,` - user process를 위해 사용되는 cpu percent  
`1.1 sy,` - kernel을 위해 사용되는 cpu percent
`0.0 ni,` - low-priority process percent
`93.2 id,`  - idle cpu percent
`0.4 wa,` - waiting for I/O cpu percent
`Mem` - physical RAM 사용 정보
`Swap:` - swap space 사용 정보
## Controlling Processes
`xlogo` - x window system logo 출력
### interrupting a process
`Ctrl+c` - interrupts a program

### Putting Process in the Backgroud
`&` - process를 background에서 실행
``` bash
xlogo &
```
ps로 실행중인 process 확인 가능
``` bash
jih88@jih88 ~ $ ps
  PID TTY          TIME CMD
 2017 pts/0    00:00:00 xlogo
 3238 pts/0    00:00:00 ps
24904 pts/0    00:00:00 bash
```
`jobs` - 실행중인 job 확인 가능
``` bash
jih88@jih88 ~ $ jobs
[1]+  실행중               xlogo &
```
### Returning a Process to the Foreground
`fg` - 실행 중인 backgrond process를 foreground로 위치시킴
``` bash
jih88@jih88 ~ $ jobs
[1]+  실행중               xlogo &
jih88@jih88 ~ $ fg %1
xlogo
^C
```
### Stopping(Pausing) a Process
`Ctrl+z` - Foreground process를 stop 시킴.
`bg` - Foreground process를 backgrond로 위치시킴.
``` bash
jih88@jih88 ~ $ xlogo
^Z
[1]+  정지됨               xlogo
jih88@jih88 ~ $ bg %1
[1]+ xlogo &
```
## Signals
`kill` - 종료하고 싶은 프로그램들을 제거함.
``` bash
jih88@jih88 ~ $ xlogo &
[1] 3643
jih88@jih88 ~ $ kill 3643
```
kill command는 signal을 전송 
`Ctrl+z`나 `Ctrl+c`와 같은 커맨드로 signal을 전송  
`Ctrl+C` - INT(Interrupt)
`Ctrl+Z` - TSTP(terminal stop)
### Sending Signals to Processes with kill
``` bash
kill [-signal] PID ...
```
1(HUP) - Hanupup, reinit할 때 많이 쓰임  
2(INT) - Interrupt, 프로그램 종료  
9(KILL) - Kill, 프로그램이 직접 종료하지 않고, kernel이 종료시킴. 다른 termination signal이 안 먹힐 때 쓰는 것이 좋음.  
15(TERM) - Terminate, kill command가 발생시키는 default 시그널. 프로그램이 signal을 받아서 종료시킴.  
18(CONT) - Continue, TSTP 시그널에 의해 정지된 process를 run시킴.  
19(STOP) - Stop, kernel에 의하여 process를 정지시킴.  
20(TSTP)- Terminal Stop, 프로그램에 의해 process를 정지시킴.  
``` bash
jih88@jih88 ~ $ xlogo &
[1] 6015
jih88@jih88 ~ $ kill -1 6015
jih88@jih88 ~ $ 
[1]+  끊어짐               xlogo
```
``` bash
jih88@jih88 ~ $ xlogo &
[1] 6048
jih88@jih88 ~ $ kill -INT 6048
jih88@jih88 ~ $ 
[1]+  인터럽트            xlogo
jih88@jih88 ~ $ xlogo &
[1] 6054
jih88@jih88 ~ $ kill -SIGINT 6054
jih88@jih88 ~ $ 
[1]+  인터럽트            xlogo
```
#### other common signal
3(QUIT) - Quit
11(SEGV) - Segnmentation Violation
28(WINCH) - Window Change
``` bash
jih88@jih88 ~ $ kill -11 6130
jih88@jih88 ~ $ 
[1]+  세그멘테이션 오류 (core dumped) xlogo
jih88@jih88 ~ $ kill -3 6156
jih88@jih88 ~ $ 
[1]+  끝내기               (core dumped) xlogo
```
``` bash
jih88@jih88 ~ $ kill -l
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
 6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
63) SIGRTMAX-1	64) SIGRTMAX	
```
### Sending Signals to Multiple Processes with killall
``` bash
killall [-u user] [-signal] name ...
```
``` bash
jih88@jih88 ~/proj/mediatek/trunk $ xlogo &
[1] 6341
jih88@jih88 ~/proj/mediatek/trunk $ xlogo &
[2] 6342
jih88@jih88 ~/proj/mediatek/trunk $ killall xlogo
[1]-  종료됨               xlogo
[2]+  종료됨               xlogo
```
## Shutting Down the System
`halt`, `poweroff`,`reboot`,`shutdown` -> reboot 혹은 종료 명령어
ex)
``` bash
sudo reboot
sudo shutdown -h now
sudo shutdown -r now
```
## More Process-Related Commands
`pstree` - process list를 tree 형태로 출력
`vmstat` - resource 사용 상황을 출력, time delay 설정 가능
``` bash
jih88@jih88 ~ $ vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0 668672 2565100 5541620 3912476    0    1    55    70    2    3  5  1 93  0  0
 0  0 668672 2565100 5541620 3912476    0    0     0     0  719 1212  1  1 98  0  0
 0  0 668672 2565100 5541620 3912476    0    0     0     0  682 1216  1  0 99  0  0
 2  0 668672 2564968 5541620 3912476    0    0     0     0  668 1135  1  0 98  0  0
```
`xload` - system load를 gui graph로 출력
`tload` - system load를 tui graph로 출력