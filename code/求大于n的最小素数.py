# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 22:04:50 2018

@author: QJ
"""

##任意输入一个正整数n，并找出大于n的最小素数
import math
m=input('请输入一个正整数')
n=int(m)
while True:
    n+=1
    print(n)
    f=True
    a=2
    while a<n:
        if n%a==0:break
        a+=1
    if f:
        print('大于%s的最小素数是%s'%(m,n))
        break