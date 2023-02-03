# rsyslog
rsyslog config 파일 위치: /etc/rsyslog.conf
중복된 syslog 제거 기능: RepeatedMsgReduction
ex)
$RepeatedMsgReduction on
remote syslog 확인:
tail -f /var/log/syslog로 확인.
시스템 로그도 함께 출력되므로 주의 필요.

# logrotate
## logrotate란
linux에서 구동되는 log 파일을 기간별로 목적별로 관리하기 위하여 백업해 주는 데몬
## 강제 로테이트 명령어
``` bash
$ logrotate -vf CONFIG_FILE
$ logrotate -f /etc/logrotate.conf
```