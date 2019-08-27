# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:17:24 2018

@author: QJ
"""

##输出50以内的勾股数
import math 
n=1
for x in range(1,51):
    y=x
    while y<=50:
       z=(x**2+y**2)**(1/2)
       ##取z整数部分判断是否为整数
       T=(math.trunc(z)==z)
       if T==True and z<=50 :
           if n<=6:
               print(x,y,math.trunc(z),sep=',',end='    ')
               n+=1
           else:
               n=2
               ##换行
               print()
               print(x,y,math.trunc(z),sep=',',end='    ')
       y+=1
      
   

