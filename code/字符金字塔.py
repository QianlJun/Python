# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 12:50:28 2018

@author: QJ
"""

##字符金字塔
for i in range(1,10):
    print(' '*(15-i),end='')
    AB=['X','A','B','C','D','E','F','G','H','I']
    a=i
    while i>=1:
        A=AB[i]
        print(A,end='')
        i-=1
    i+=2
    while i<=a:
        A=AB[i]
        print(A,end='')
        i+=1
    print()
AB=['A','B','C','D','E','F','G','I']
A=AB[0]
A
print(A)
