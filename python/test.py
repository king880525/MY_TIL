import random

class test:
    def __init__(self):
        self.blacklist=[]
        self.whitelist=[]
        self.destlist=[]
        self.maxnum=6
    def blacklist_add(self,num):
        self.blacklist.append(num)
        self.blacklist.sort()
    def whitelist_add(self,num):
        self.whitelist.append(num)
        self.whitelist.sort()
    def blacklist_print(self):
        print(self.blacklist)
    def whitelist_print(self):
        print(self.whitelist)
    def generator(self) :
        randlist=[]
        for i in range(1,48):
            randlist.append(i)
        for num in self.whitelist:
            randlist.remove(num)
        for num in self.blacklist:
            randlist.remove(num)
        randnum = self.maxnum
        randnum -= len(self.whitelist)
        self.destlist = self.whitelist[:]
        self.destlist += random.sample(randlist, randnum)
        self.destlist.sort()
        print(self.destlist)

class test_tui(test):
    def tui(self):
        while 1 :
            print("============")
            print("generator")
            print("============")
            print("1. blacklist 추가")
            print("2. whitelist 추가")
            print("3. generate")
            print("other. exit")
            a = input("동작을 입력하세요.: ")
            if a == "1":
                num = input("숫자를 입력하시오: ")
                self.blacklist_add(int(num))
                self.blacklist_print()
            elif a =="2":
                num = input("숫자를 입력하시오: ")
                self.whitelist_add(int(num))
                self.whitelist_print()
            elif a =="3":
                self.generator()
            else:
                break

mytest = test_tui()
mytest.tui()