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