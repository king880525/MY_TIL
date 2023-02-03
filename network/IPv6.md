## IPv6 이론
- 128bit 크기를 가지고 있다.
- 16진수로 표현하기 때문에 총 32자리의 숫자로 표현된다.
- 16진수 4개의 숫자마다 :(콜론)을 써서 구분한다.
- Leading 0s: 앞에 오는 0들을 생략할 수 있다.
(2001:0000:0000:00A1:0000:0000:0000:1E2A → 2001:0:0:A1:0:0:0:1E2A)
- Consecutive 0s: 연속되는 0을 생략할 수 있다.
(2001:0:0:A1:0:0:0:1E2A → 2001:0:0:A1::1E2A)
![ipv6_structure](/network/image/ipv6_addr_structure.png)
- Network Prefix: Network ID
- Interface ID: Host ID
-   IPv4와 다르게 Subnet Mask는 사용하지 않는다.
## ipv6 Header

## ipv6 메모
크게 두 가지 방식으로 나뉜다.
1) Statefull - mgmt flag 1 
2) Stateless - mgmt flag 0
3. 도메인 정보로 DNS Query -> attr_server IP 획득(IPv6 주소)
4. 터널 생성: 터널 interface
v6 Header/v4 Header

## ipv6 링크
https://peemangit.tistory.com/160
https://zigispace.net/386
https://meetup.toast.com/posts/91
- ipv6에서의 arp 동작  
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=nackji80&logNo=221321190805


## 참고 URL들
https://linux.die.net/man/5/radvd.conf
https://tldp.org/HOWTO/Linux+IPv6-HOWTO/ch22s04.html
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_the_radvd_daemon_for_ipv6_routers
https://blueamor.tistory.com/123
https://openwrt.org/ko/docs/guide-user/ipv6_ipv4_transitioning
https://superuser.com/questions/1324060/use-radvd-to-advertise-google-or-any-ipv6-dns-addresses-to-all-clients
https://www.isc.org/blogs/ds-lite-architecture-overview-and-automatic-configuration/
https://github.com/radvd-project/radvd/blob/master/radvd.conf.example
https://datatracker.ietf.org/doc/html/rfc2461
https://en.wikipedia.org/wiki/Radvd
https://github.com/barteqpl/openwrt-ipv6
https://yyman.tistory.com/1513?category=204127
https://yyman.tistory.com/1514?category=204127
https://tech.ktcloud.com/66
https://datatracker.ietf.org/doc/rfc4703/
https://docs.qnap.com/operating-system/qts/5.0.x/ko-kr/ddns-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%84%A4%EC%A0%95-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0-7F03EB91.html
