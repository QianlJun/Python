# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:38:28 2018

@author: QJ
"""

#calculate n!
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
fact(4)

#calculate n!//m
def fact2(n,m=1):
    s=1
    for i in (1,n+1):
        s *=i
    return s//m

#计算n!乘数
def fact3(n,*b):
    s=1
    for i in range(1,n+1):
        s *=i
    for item in b:
        s *=item
    return s 

#函数返回0个或多个值
def fact2(n,m=1):
    s=1
    for i in (1,n+1):
        s *=i
    return s//m,n,m
a,b,v=fact2(10,5)
print(a,b,c)

#全局变量和局部变量
n,s = 10, 100
def fact(n):
    global s
    for i in range(1,n+1):
        s *=i
    return s 
print(fact(n),s)

#局部变量为组合数据类型且未创建，等同于全局变量
ls = ["F","f"]
def func(a):
    ls.append(a)
    return
func("C")
print(ls)

ls = ["F","f"]
def func(a):
    ls=[]
    ls.append(a)
    return
func("C")
print(ls)

#定义lambda函数
f=lambda x,y : x+y
f(10,15)

f=lambda : "lambda函数"
print(f())






























