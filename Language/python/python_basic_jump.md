# 개요
jump to python 책 공부 정리  
모르거나 어려운 개념만 정리  
# list type check 루틴
``` python
a = [1,[2,3],[1,2,3]]
for i in range(0, len(a)):
    print("a[%d]: " % i+ str(a[i]))
    if str(type(a[i])) == "<class 'list'>":
        for j in range(0, len(a[i])):
            print("a[%d][%d]: " % (i,j)+ str(a[i][j]))
```
# 모듈을 불러오는 또 다른 방법
우리는 지금껏 명령 프롬프트 창을 열고 모듈이 있는 디렉터리로 이동한 다음에 모듈을 사용할 수 있었다. 
이번에는 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법에 대해 알아보자.

먼저 다음과 같이 이전에 만든 mod2.py 파일을 C:\doit\mymod로 이동시킨다.
``` bash
C:\Users\pahkey>cd C:\doit
C:\doit>mkdir mymod
C:\doit>move mod2.py mymod
```
1개 파일을 이동했습니다.
그리고 다음 예를 따라 해 보자.

## 1. sys.path.append(모듈을 저장한 디렉터리) 사용하기
먼저 sys 모듈을 불러온다.
``` python
C:\doit>python
>>> import sys
```
sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다.  
sys에 대해서는 뒤에서 자세하게 다룰 것이다.  
이 sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다. 

다음과 같이 입력해 보자.
``` python
>>> sys.path
['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs', 
'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages']
```
sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다. 
만약 파이썬 모듈이 위 디렉터리에 들어 있다면 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러서 사용할 수 있다. 
렇다면 sys.path에 C:\doit\mymod 디렉터리를 추가하면 아무 곳에서나 불러 사용할 수 있지 않을까?
※ 명령 프롬프트 창에서는 /, \든 상관없지만, 소스 코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다.
당연하다. sys.path의 결괏값이 리스트이므로 우리는 다음과 같이 할 수 있다.
``` python
>>> sys.path.append("C:/doit/mymod")
>>> sys.path
['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs', 
'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages', 
'C:/doit/mymod']
>>>
```
sys.path.append를 사용해서 C:/doit/mymod라는 디렉터리를 sys.path에 추가한 후 다시 sys.path를 보면 
가장 마지막 요소에 C:/doit/mymod라고 추가된 것을 확인할 수 있다.

자, 실제로 모듈을 불러와서 사용할 수 있는지 확인해 보자.
``` python
>>> import mod2
>>> print(mod2.add(3,4))
7
```
이상 없이 불러와서 사용할 수 있다.

## 2. PYTHONPATH 환경 변수 사용하기
모듈을 불러와서 사용하는 또 다른 방법으로는 PYTHONPATH 환경 변수를 사용하는 방법이 있다.
다음과 같이 따라 해 보자.
``` python
C:\doit>set PYTHONPATH=C:\doit\mymod
C:\doit>python
>>> import mod2
>>> print(mod2.add(3,4))
7
```
set 명령어를 사용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 C:\doit\mymod 디렉터리를 설정한다. 
그러면 디렉터리 이동이나 별도의 모듈 추가 작업 없이 mod2 모듈을 불러와서 사용할 수 있다.