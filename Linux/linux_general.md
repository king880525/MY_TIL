# 명령어
## 항상 헷갈리는 심볼링 링크
`ln -s [경로명] [심볼릭 링크 이름]`
ex) `ln -s ~/test test_sym`
## scp 명령어 
ssh를 이용한 파일 전송
`scp [host]@[ip]:[path] [copy_dest]`
ex) `scp jih88@222.117.116.182:/tmp/symbolic/tftp/last ./`
## fail2ban 확인
### 1. 차단 현황을 확인
`#fail2ban-client status`
Status
Number of jail: 1
Jail list: sshd
위 내용에서 현재 블럭되어있는 IP갯수가 1개임을 확인 할 수 있다.
(IP정보도 함께 보여주면 좋을것 같은데)

### 2. 차단된 IP정보 확인
`#vi /var/log/fail2ban.log`
위 로그에서 "[sshd] Ban xxx.xxx.xxx.xxx" 형태로 남아있는 로그를 찾아서 IP정보를 확인한다.
혹은 아래의 명령으로 한번에 확인할 수도 있다.
`# cat /var/log/fail2ban.log* | grep "] Ban" | awk '{print $NF}' | sort | uniq -c | sort -n`

### 3.  fail2ban 차단ip 해제하기
`# [root@victor jail.d]# fail2ban-client set sshd unbanip 221.xxx.xxx.xxx`
fail2ban을 재시작하지않아도 바로 접속이 가능해진다.

# 링크
bash shell script 강좌
https://wikidocs.net/book/2370