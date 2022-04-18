# 개요
보안 메뉴의 네트워크 보안 관련 정리 문서
# Flooding
- 많은 양의 traffic을 특정 서버 혹은 서비스로 전송하는 행위
- 혹은 많은 양의 traffic을 특정 네트워크 세그먼트로 전송하는 행위
- 네트워크를 마비시키거나, 네트워크가 마비된 틈을 타서 변조된 패킷을 전송함으로서 정보를 탈취하기 위한 목적으로 발생
## 링크
https://www.sciencedirect.com/topics/computer-science/flooding-attack
# Spoofing
- 공격자가 공격대상을 속여서 공격하는 방법
- 시작 주소나 목적 주소 등을 속여서 대상의 정보를 탈취하기 위한 목적으로 발생
## 링크
https://sonseungha.tistory.com/486  
# DOS 공격
- Deinal Of Service의 약자, 서비스 거부 공격
- 시스템을 악의적으로 공격해 해당 시스템의 리소스를 부족하게 하여 원래 의도된 용도로 사용하지 못하게 하는 공격
- 대량의 데이터 패킷을 통신망으로 보내고, 특정 서버에 수많은 접속 시도를 하는 등, 다른 사용자가 서비스 이용을 하지 못 하게 하는 공격
# DDOS 공격
- Distributed Denial Of Service의 약자
- 여러대의 공격자를 분산적으로 배치해 동시에 서비스 거부 공격(D0S)을 하는 방법
## 링크
https://ko.wikipedia.org/wiki/%EC%84%9C%EB%B9%84%EC%8A%A4_%EA%B1%B0%EB%B6%80_%EA%B3%B5%EA%B2%A9
# ICMP Flood
- 대량의 ICMP 패킷을 서버로 전송
- 서버가 보유한 네트워크 대역폭을 가득 채워 정상적인 클라이언트의 접속 차단
- 출발지 IP를 위조한 다량의 ICMP 패킷을 타겟서버로 발생
## 링크 
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=on21life&logNo=221528979203
# UDP Flood
- DDOS 공격의 일종. 대량의 UDP 패킷을 이용하여 호스트의 네트워크 자원 소모
- 네트워크의 bandwidth를 소모시키는 것이 목적.
## 링크
https://blog.naver.com/PostView.nhn?blogId=wnrjsxo&logNo=221338322734
# SYN Flood
- TCP 연결과정(3way handshake)의 취약점을 이용한 공격
- 과도한 TCP SYN 패킷을 서버에 전송하여 Server에 부하를 발생시켜 제기능을 못 하도록 함.
## 링크
https://crossjin.tistory.com/entry/TCP-SYN-Flooding-%EA%B3%B5%EA%B2%A9-%EC%9D%B4%EB%9E%80
https://run-it.tistory.com/51
# ARP Flood
- 스위치의 CAM 테이블에 엄청난 양의 ARP 응답을 보내 과부하시키는 방법
## 링크
https://www.rfwireless-world.com/Articles/ARP-attack-types-MAC-flooding-and-ARP-Spoofing.html
# IP Spoof

## 링크
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wnrjsxo&logNo=221111232129
# IP Sweep
- ping Sweep
- 대상 네트워크의 서버를 파악하기 위해 공격자가 icmp를 이용하여 broadcast ping을 날려서 network의 ip 파악
- 네트워크 자체를 마비시키기 위해서도 사용.
- broadcast ping과 유사 기능
## 링크
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=twers&logNo=50117821768
# 포트 스캔
- 네트워크에 연결된 컴퓨터의 모든 포트를 자동으로 검색
- 열린 포트를 감지하여 공격을 수행
## 링크
https://itigic.com/ko/what-are-port-scan-attacks-and-how-to-avoid-them/
# 출발지 IP/ 목적지 IP 세션 제한
- IP당 세션 개수를 제한
- 동시에 발생되는 트래픽의 개수를 제한
- Torrent/dos 좀비 공격을 막을 수 있다.
## 링크
https://www.2cpu.co.kr/QnA/416361
# TCP SYN Attack
- SYN Flood와 동일
## 링크
https://www.cloudflare.com/ko-kr/learning/ddos/syn-flood-ddos-attack/
# ARP Spoofing
- 공격자가 클라이언트가 서버에 보내는 패킷을 받은 뒤, 서버에게 패킷 전송
- 자신의 MAC 주소를 속여서, 서버에게 보내는 방식
- 자신의 주소가 아님에도 ARP 신호를 보내는 패킷을 보내는 현상을 이용해 탐지.
- 일정량 이상의 ARP 차단
## 링크
https://security-nanglam.tistory.com/191
# Trace Route 응답
- 목적지까지의 routing 경로를 알아내기 위한 traceroute 명령에 대한 응답을 차단.
# Broadcast Ping 응답
- icmp를 broadcast로 송신하여 해당 네트워크 내에 접속한 모든 IP를 알아내서, 이를 이용해 smurf 공격 실행
- 이를 방지하기 위해 broadcast로 전달받은 ping 차단하는 기능
## 링크
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=01191879872&logNo=10017633786
# Ping of Death
- 규정 크기 이상의 icmp 패킷으로 시스템을 마비시키는 공격
- 크기가 큰 패킷은 분할되어 목적지로 전송되고, 수많은 패킷을 받은 공격 대상은 부하가 발생하여 마비됨.
- icmp 패킷 블로킹 설정으로 피할 수 있음.
## 링크
https://run-it.tistory.com/52
# 웜 바이러스 차단
- 웜 바이러스 Attack을 위해 이용되는 내부로 향하는 TCP Port drop
