# docker란
가상 컨테이너.
다른 개발환경을 가상으로 실행하여 사용할 수 있다.
# docker 이미지 찾기
```
docker search ubu
```
# docker 이미지 다운
```
docker pull [옵션] [경로]<이미지명>[:태그명]
```
ex)
```
docker pull ubuntu
```
# docker 다운 받은 이미지 확인
```
$ docker images
```

# docker 이미지로 컨테이너 실행
```
$ docker create [옵션] <이미지명> [명령어] [인자..]
```
ex)
```
$ docker create --name con_ubuntu ubuntu
```
# 생성된 컨테이너 실행
```
$ docker start [옵션] <컨테이너명> [컨테이너명2...]
```
ex)
```
$ docker start con_ubuntu
```
## docker 이미지 사용 방법
1. pull을 이용해 이미 생성된 이미지 로드
2. 컨테이너의 변경사항으로 이미지를 만든다.
3. DockerFile을 빌드한다.
# docker file 빌드 방법
ex)
1) docker file을 아래와 같이 작성
<code> FROM ubuntu:bionic 
RUN apt-get update 
RUN apt-get install -y git</code>
2) dockerfile로 이미지 빌드
``` bash
$ docker build -t ubuntu:git-from-dockerfile .
```

# 링크
우분투 허브
https://hub.docker.com/_/ubuntu
CentOS 허브
https://hub.docker.com/_/centos
문서 작성 참조 링크
https://sleepyeyes.tistory.com/67

## 참고도서
http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791165215743&orderClick=LAG&Kc=