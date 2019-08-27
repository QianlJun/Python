# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 20:55:14 2018

@author: QJ
"""
##输出10个两位的随机素数
import random
n=0
while n<10:
    x=random.randint(10,99)
    #判断x是否为素数
    a=2
    while a<x-1:
        if x%a==0:break
        a+=1
    else:
        print(x,end=' ')
        n+=1
##自己编写的
import random
n=0
while n<10:
    x=random.randint(10,99)
    a=2
    while a<x: 
        if x%a==0:break
        a+=1
    else:
        print(x,end=' ')
        n+=1
