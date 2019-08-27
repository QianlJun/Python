# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 20:10:55 2018

@author: QJ
"""

##输出数字金字塔
for x in range(1,10):
    print(' '*(15-x),end='')
    n=x
    while n>=1:
        print(n,sep='',end='')
        n-=1
    n+=2
    while n<=x:
        print(n,sep='',end='')
        n+=1
    print()
x=1
15-x
*(15-x)
print(*(15-x))
for x in range(1,10):
    print(' '*(15-x),end='')
for x in range(1,10):
    print(' '*(15-x),end='')
    n=x
    while n>=1:
        print(n,end='')
        n-=1
    n+=2
    while n<=x:
        print(n,end='')
        n+=1
    print()