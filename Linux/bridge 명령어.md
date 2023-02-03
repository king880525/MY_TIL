## bridge 명령어
bridge 주소 및 장치를 출력하거나, 설정할 수 있는 명령어
ex)
``` bash
/ # bridge fdb show
01:00:5e:00:00:01 dev ifb0 self permanent
01:00:5e:00:00:01 dev eth0 self permanent
70:5d:cc:f5:85:4a dev eth0.2 master br0 
01:00:5e:00:00:01 dev eth0.2 self permanent
01:00:5e:00:00:01 dev eth0.3 self permanent
88:36:6c:f3:52:86 dev eth0.4 master br0 
01:00:5e:00:00:01 dev eth0.4 self permanent
01:00:5e:00:00:01 dev eth0.5 self permanent
01:00:5e:00:00:01 dev nas0 self permanent
01:00:5e:7f:66:12 dev nas0 self permanent
e2:11:85:06:5f:e4 dev wlan0 master br0 
da:7a:17:e4:bc:8b dev wlan0 master br0 
8a:46:36:16:fe:27 dev wlan0 master br0 
33:33:00:00:00:01 dev wlan0 self permanent
01:00:5e:00:00:01 dev wlan0 self permanent
82:08:9a:c3:75:0d dev wlan1 master br0 
00:08:52:fd:59:23 dev wlan1 master br0 permanent
e6:7b:40:1c:b0:de dev wlan1 master br0 
33:33:00:00:00:01 dev wlan1 self permanent
01:00:5e:00:00:01 dev wlan1 self permanent
01:00:5e:00:00:01 dev br0 self permanent
01:00:5e:7f:ff:fa dev br0 self permanent
01:00:5e:00:00:02 dev br0 self permanent
01:00:5e:00:00:16 dev br0 self permanent
00:08:52:fd:59:1d dev br0 master br0 permanent
a2:c8:89:30:10:d9 dev wlan0-vap0 master br0 
00:08:52:fd:59:1e dev wlan0-vap0 master br0 permanent
33:33:00:00:00:01 dev wlan0-vap0 self permanent
01:00:5e:00:00:01 dev wlan0-vap0 self permanent
```

### 참조 링크
man page
https://man7.org/linux/man-pages/man8/bridge.8.html