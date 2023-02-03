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

sudo docker ps -a

docker server에서 image 가져오기
docker pull 172.17.122.17:5000/buildspace_miru

docker images

image로 container만들기 (run)
docker run -it --name buildspace -v /home/ygjeon:/home/ygjeon -v /media:/media 172.17.122.17:5000/buildspace_miru /bin/bash

container 접속 후 종료
ygjeon@ygjeon-desktop ~ $ docker start buildspace
buildspace
ygjeon@ygjeon-desktop ~ $ docker attach buildspace
root@0acd35d60fb2 / # 

attach후 'exit'로 종료하면 container 종료됨
start만 하면 background로 살아있음

container 백그라운드 실행 후, 접속
docker start buildspace
buildspace

docker exec -it buildspace /bin/bash 

## 1. 최초 설정

docker run -it --name SDK.11.5 -v /home/jih88:/home/jih88 -v /media:/media 172.17.122.1:5000/qca_sdk_11.5.csu1 /bin/bash

## 2. 이미지 설치 과정
### 이미지 가져오기
``` bash
docker pull 172.17.122.1:5000/buildspace_miru
```
### 이미지 확인
``` bash
docker images
```
### 이미지로 컨테이너 만들기
``` bash
docker run -it --name SDK.11.5 -v /home/jih88:/home/jih88 -v /media:/media 172.17.122.1:5000/qca_sdk_11.5.csu1 /bin/bash
```
### 컨테이너 확인
``` bash
# 실행 컨테이너 확인
docker ps
# 모든 컨테이너 확인
docker ps -a
```
## 3. 컨테이너
### 컨테이너 실행
``` bash
docker start SDK.11.5
```
### 컨테이너 백그라운드 RUN
``` bash
docker exec -it SDK.11.5 /bin/bash
```
### 컨테이너 포그라운드 RUN
``` bash
docker attach SDK.11.5
```
## 4. 삭제
### 1. 컨테이너 삭제
``` bash
# container id 확인
docker ps -a
# container id를 참조하여 삭제
docker rm ${CONTAINER_ID}
```
### 2. 이미지 삭제
``` bash
# image 정보 확인
docker images -a
# image 정보를 참조하여 삭제
docker rmi ${REPOSITORY}:${TAG}
docker rmi ${IMAGE_ID}
# Container까지 한 번에 삭제
docker rmi -f ${IMAGE_ID}
```

링크
https://www.daleseo.com/docker-containers/
