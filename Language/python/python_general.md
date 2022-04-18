# 강좌 링크
python 기초 강좌  
https://wikidocs.net/book/1  

python UI 강좌 사이트  
https://wikidocs.net/book/2165  

python 라이브러리 강좌  
https://wikidocs.net/book/5445  

python 웹서버 강좌  
장고  
https://wikidocs.net/book/4223  

플라스크  
https://wikidocs.net/book/4542  

Python Essential Reference"와 "Python Cook Book" 의 공개 python 강좌 "Practical Python"  
https://wikidocs.net/82391

# 에러 수정
## 1. except , syntax error
``` bash
  File "update_common_info.py", line 142
    except ModemPartitionSizeNotFoundException , ex:
                                               ^
SyntaxError: invalid syntax
```
- 참조
https://antilibrary.org/863
- 이유  
python3에서는 더 이상 ,로 구분하는 것을 허용하지 않기 때문에
,를 as로 대체한다.
``` bash
except ModemPartitionSizeNotFoundException as ex:
```
## 2. python 버전 선택
python2와 python3의 버전이 많이 다르기 때문에  
python2 기준으로 작성된 코드를 python3로 실행하면 에러 발생  
버전 변경 방법은 우분투 기준으로 아래 코드 실행.
``` bash
sudo update-alternatives --config python
```
