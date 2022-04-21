# 명령어
`git status` -> 상태 표시
`git status -uno` -> 관리되고 있는 파일의 상태만 표시
# 설치 후 설정
 ``` bash
$ git config --global user.name "Your Name"
$ git config --global user.email you@example.com
```
# git config 확인
``` bash
$ cat ~/.gitconfig
[user]
    name = Your Name
    email = you@example.com
```

# Token 문제로 Git Clone 오류 시 대처 방법
## 에러 로그
``` bash
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/king880525/python_study.git/'
```
## 링크
https://snepbnt.tistory.com/540