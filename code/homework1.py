# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:17:34 2018

@author: QJ
"""

print("Hello World")

print("H\ne\nl\nl\no\n \nW\no\nr\nl\nd")

a = input()
a=eval(a)
print(a**0,a**1,a**2,a**3,a**4,a**5)
type(a)

TempStr=input()
if TempStr[0] in ['C']:
    F=eval(TempStr[1:])*1.8+32
    print("F{:.2f}".format(F))
elif TempStr[0] in ['F']:
    C=((eval(TempStr[1:])-32)/1.8)
    print("C{:.2f}".format(C))

Cury=input()
if Cury[0:3] in ['RMB']:
    USD=eval(Cury[3:])/6.78
    print("USD{:.2f}".format(USD))
elif Cury[0:3] in ['USD']:
    RMB=eval(Cury[3:])*6.78
    print("RMB{:.2f}".format(RMB))

print("祖国，您好！\n我来了，学好Python。")

heat = input()
if heat[-1] in ['J']:
    cal=eval(heat[0:-1])/4.186
    print("{:.3f}cal".format(cal))
elif heat[-3:] in ['cal']:
    J=eval(heat[0:-3])*4.186
    print("{:.3f}J".format(J))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    