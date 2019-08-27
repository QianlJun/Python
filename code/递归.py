# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 21:09:06 2018

@author: QJ
"""

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
fact(5)

#字符串的反转
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]
rvs("python")

#斐波那契数列
def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

#汉诺塔
count =0
def hanoi(n,src,dst,mid):
    global count
    if n==1:
        print("{}:{}->{}".format(1,src,dst))
        count +=1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count +=1
        hanoi(n-1,mid,dst,src)
hanoi(3,"A","B","C")
print(count)
























