## port forwarding, dmz, superdmz 차이점
- 구현도 했었는데 까먹어서 다시 정리
### port forwarding
- ap 외부에서 ap의 ip의 특정 포트로 접속할 경우, ap에 연결된 단말의 특정 포트로 넘겨줌
- iptable redirect 룰로 구현
###  dmz
- ap 외부에서  ap의 ip로 접속할 경우, 모든 포트에 대한 접속을 특정 단말로 넘겨줌.
- 이 때 단말은 내부 ip 사용.
- iptable redirect 룰로 구현
### superdmz
- 단말에 ap의 외부 ip를 할당하고 ap 외부에서 외부 ip로 접속하는 모든 연결을 해당 단말로 보냄.
- 단말이 ap 자체인 것처럼 동작.
- arp를 proxy로 넘겨 주며,