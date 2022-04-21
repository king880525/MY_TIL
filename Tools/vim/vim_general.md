# 명령어
## 치환
```
: 시작행,끝행s/원래문자열/변경문자열/옵션 
```
ex)
38번째 줄부터 385번째 줄까지 MTWF_LOG를 printk로 치환
``` bash
:38,385s/MTWF_LOG/printk/g
```
1~10행의 모든 Hello를 Bye로 변경 - 
``` bash
:1,10s/Hello/Bye/g
```
문서 전체의 모든 Hello를 Bye로 변경
``` bash
:%s/Hello/Bye/g
```
현재 행에서 마지막 행 까지의 모든 Hello를 Bye로 변경
``` bash
:.,$s/Hello/Bye/g
```
## line number
`set nu` - 라인 넘버 표시  
`set nu!` - 라인 넘버 미표시

## 탭 문자, 개행 문자 표시
`set list` - tab, 개행 문자 표시
`set nolist` - tab, 개행 문자 미표시

## line control
커서 끈 상태에서 J : 여러 줄을 한 줄로 합침.

## 링크
vim 도대체 왜 쓰는가
https://bengi.kr/1349
vim 어드벤쳐
https://vim-adventures.com/