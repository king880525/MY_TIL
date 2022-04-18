# procd init script 작성
- 아래 구문을 꼭 붙여줘야 한다. (서비스 start가 안 됨.)
``` bash
#!/bin/sh /etc/rc.common
```
-  모든 파라미터 등의 정보는 procd에 의해 내부적으로 저장된다.
-  Init script has to specify all possible procd events that may require service reconfiguration. Defining all triggers is done in the service_triggers() using procd_add_*_trigger helpers.
## 관련 링크
https://openwrt.org/docs/techref/procd
https://openwrt.org/docs/guide-developer/procd-init-scripts