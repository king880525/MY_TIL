## Crypt

### 개요
패스워드를 만드는데 사용되는 함수  
hash를 이용한 단방항 암호화 방식이다.

### 함수 원형
``` c
#include <unistd.h>

char *crypt(const char *key, const char *salt);
```
key - 암호화 하고 싶은 평문 key 
salt - 첫번째 두 글자를 salt로 사용.

### 참조링크
리눅스 decription
https://pubs.opengroup.org/onlinepubs/7908799/xsh/crypt.html
예제 1
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=endfirst&logNo=20007936076
크래킹 예제
https://songker.tistory.com/entry/%ED%8C%A8%EC%8A%A4%EC%9B%8C%EB%93%9C-%ED%81%AC%EB%9E%99%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EC%9D%98-%EC%9B%90%EB%A6%AC
예제 2
https://kldp.org/node/1095