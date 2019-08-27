# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:42:12 2018

@author: QJ
"""

a=5
a+=10
a
x={1,2,3}
type(x)
set({1,2,3})
{1,2,3,1}
{1:4}
{x for x in (1,2,3,4)}
x={1,2,3}
for a in x:print(a)
x=frozenset({1,2,3})
x
print(x)
y=set({4,5})
y
y.add(x)
print(y)
x=str(123)
x
type(x)
x="""This is 
a Python
multiline string"""
x
print(x)
'12' '34' '56'
'12'+'34'+'56'
'12'*3
for a in 'abc':print(a)
for a in {123}:print(a)
x='abcdef'
x[0]
x='abcdef'
x[1:4]
x[:4]
x[1: :2]
x='0123456789'
x[1:7:2]
x[::2]
x[7:1:-2]
x[::-1]
'this is Python'.capitalize()
'My name is {0},age is {1}'.format('Tom',23)
x='ab12'*4
x
x.replace('12','000')
x.replace('12','00',2)
"The %s's price id %4.2f"%('apple',2.5)
'123%c%c'%("a",65)
[range(1,3)]
list(range(-2,3))
list(x+10 for x in range(5))
x=list(range(10))
x=[1,2,3,4,5,6]
del x[0]
x
y=x.copy()
y
y=x
y
del x[0]
x
y
for a in range(1,10,2):print(a)
dict({'name':'John','age':25,'sex':'male',})
2*3+4
2+3*4
5/2
5//2
x='abc'
y=x
y=100
print(y)
print(x)
y=x
y[0]=100
print(x)
y[0]
x=('max','min')
y=(100,0)
a=dict(zip(x,y))
y
x
a
print(a)
a['min']=-100
a
del a['max']
print(a)
x=[11,22,33,44,55]
myfile=open(r'c:\Users\QJ\Desktop\listdata.dat','w')
myfile.write(x)
myfile.writelines(x)
import pickle
pickle.dump(x,myfile)
x
type(x)
x=['11','22','33','44','55']
myfile.writelines(x)
x
myfile.close
myfile=open(r'c:\Users\QJ\Desktop\listdata.dat','r')
print(myfile.read())
myfile.close()
myfile=open(r'C:\Users\QJ\Desktop\listdata.dat','w')
myfile.writelines(['11','22'])
myfile.close()
myfile=open(r'C:\Users\QJ\Desktop\listdata.dat','r')
print(myfile.read())
myfile.read()
myfile.close()
x=[1,2,'abc']
y={'name':'John','age':25}
myfile=open(r'C:\Users\QJ\Desktop\objdata.bin','wb')
import pickle
pickle.dump(x,myfile)
pickle.dump(y,myfile)
myfile.close()
myfile=open(r'C:\Users\QJ\Desktop\objdata.bin','rb')
myfile.read()
myfile.seek(0)
x=pickle.load(myfile)
x
print(myfile.read())
print(x)
x=5
if x>0:
    print(x,'是正数')
x=-5
if x>0: 
    print(x,'是正数')
else:
    print(x,'不是正数')
x=85
if x<60:
    print('不及格')
elif x<70:
    print('及格')
elif x<90:
    print('中等')
else:
    print('优秀')
x=5
y=10
a=[x,y][x<y]
a
for x in (1,2,3,(4,5)):
    print(x)
for x in 'book':
    print(x)
for x in (1,2,3):
    print(x*2)
else:
    print('loop over')
for (a,b) in ((1,2),(3,4),(5,6)):print(a,b)
for (a,*b) in ((1,2,'abc'),(3,4,5)):print(a,b)
a=[]
n=0
for x in range(100,999):
    s=str(x)
    if s[0]!=s[-1]:continue
    a.append(x)
    n+=1
    if n==10:break
else:
    print('loop over')
print(a)
print(2,3,end="")
for x in range(4,100):
    for n in range(2,x):
        if x%n==0:
            break
    else:
        print(x,end=' ')
else:
    print('over')
s=0
n=1
while n<=100:
    s=s+n
    n=n+1
print('1+2...100=',s)
s
x=2
while x<100:
    n=2
    while n<x-1:
        if x%n==0:break
        n+=1
    else:
        print(x,end=' ')
    x+=1
else:
    print('over')
a=1
while a<10:
    b=1
    while b<=a:
        print('%d*%d=%2d'%(a,b,a*b),end=' ')
        b+=1
    print()
    a+=1
d=iter([1,2,3])
next(d)
d=iter((1,2,(3,4)))
t=[1,2,3,4]
for x in range(len(t)):
    t[x]=t[x]+10
t
t=[x+10 for x in t]
t
[x+y for x in (10,20) for y in (1,2,3)]
[x+10 for x in range(10) if x%2==0]
s=0
n=1
while n<=100:
    
    s=s+n
    n=n+1
else:
    print('1+2+...+100=',s)
x=3
a=1 if x>5 else -1
b=[1,-1][x>5]
print(a,b)
s=0
for a in range(1,5):
    for b in range(1,a):
        s+=1
print(s)
x=1
y=1
while y<=5:
    x=x*y
    y=y+2
print(x)
def hello():
    print('Python 你好')
hello()
def add(a,b):
    return a+b
add(1,2)
add
add(2,30)
def add(a,*b):
    s=a
    for x in b:
        s+=x
    return s
add(1,2,3,4)
def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
fac(3)
class testclass:
    data=100
    def setpdata(self,value):
        self.pdata=value
    def showpdata(self):
        print('self.pdata=',self.pdata)
    print('类testclass加载完成!')
type(testclass)
testclass.data
x=testclass()
x.setpdata('abc')
x.showpdata()
y=testclass()
y.setpdata(123)
y.showpdata()
x.data,y.data
testclass.data=200
x.data,y.data
dir(testclass)
dir(x)
x=testclass()
x.pdata
x.setpdata(123)
testclass.data2='abc'
x.data3=[1,2]
testclass.data2,x.data2,x.data3
dir(testclass)
class test:
    def add(a,b):return a+b
    def add2(self,a,b):return a+b
test.add(2,3)
test.add2(2,3,4)
x=test()
x.add(3,4)
class test:
    data=100
    __data2=200
    def add(a,b):
        return a+b
    def __sub(a,b):
        return a-b
test.data
test.add(2,3)
test.__data2
test.__sub(2,3)
test._test__sub(2,3)
class test:
    def __init__(self,value):
        self.data=value
        print('构造函数执行完毕!')
    def __del__(self):
        del self.data
        print('析构函数执行完毕!')
x=test(100)
x.data
del x
class test:
    def __init__(self,a):
        self.data=a[:]
    def __add__(self,obj):
        x=len(self.data)
        y=len(obj.data)
        max=x if x>y else y
        nl=[]
        for n in range(max):
            nl.append(self.data[n]+obj.data[n])
            return test(nl[:])
x=test([1,2,3])
y=test([10,20,30])
z=x+y
z.data
class test:
    def __init__(self,a):
        self.data=a[:]
    def __getitem__(self,index):
        return self.data[index]
x=test([1,2,3,4])
x[1]
x[:]
x[:2]
for a in x:print(a)
class test:
    def __init__(self,a):
        self.data=a[:]
        self.next=0
        self.end=len(a)
    def __iter__(self):
        return self
    def __next__(self):
        if self.next==self.end:
            raise StopIteration
        n=self.data[self.next]
        self.next+=1
        return n 
def dosome():
    try:
        print(5/0)
    except:
        print('出错了')
    finally:
        print('finally 部分已执行')
    print('over')
dosome()
raise IndexError
x=IndexError()
raise x
try:
    raise IndexError
except:
    print('出错了')
    raise
try:
    import math
    x=-5
    assert x>=0,'参数x必须是非负数'
except Exception as ex:
    print('异常类型: ', ex.__class__.__name__)
    print('异常信息： ',ex)
##第七章
import sqlite3
sqlite3.sqlite_version
cn=sqlite3.connect('userdata.db')
cn.execute('create table test(name varchar(10),age int(2))')
cur=cn.cursor()
cur.execute('create table test2(name varchaar(10),age int(2))')
n=cn.execute('create temp table temp(name text)')
n=cur.execute('insert into test values("John",18)')
cur.rowcount
n=cur.execute('insert into test values(?,?)',('mike',20))
n=cur.executemany('insert into test values(?,?)',[('cate',17),('tome',18)])
cur.rowcount
cn.commit()
cur=cn.execute('select * from test')
cur.fetchall()
pip scanpy-0.4.4-cp36-cp36m-win_amd64.whl
