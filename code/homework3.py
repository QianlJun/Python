# -*-") coding: utf-8 -*-
"""
Created on Fri Apr 27 16:56:10 2018

@author: QJ
"""

#Programming
N= input()
N=eval(N)**2
print("{:-^20}".format(N))

#2
N=input()
N=eval(N)
Nabs=abs(N)
if N>=0:
    Nplus=abs(N)+10
    Nminus=abs(abs(N)-10)
    Nmultiply=abs(N)*10
elif N<0:
    Nplus=-(abs(N)+10)
    Nminus=-abs((abs(N)-10))
    Nmultiply=-(abs(N)*10)
print("{:d} {:d} {:d} {:d}".format(Nabs,Nplus,Nminus,Nmultiply))


#3
N=input()
DayUp=1
DayDown=1
for i in range(365):
    DayUp=DayUp*(1+eval(N)*0.001)
    DayDown=DayDown*(1-eval(N)*0.001)
Ratio=int(DayUp/DayDown)
print("{:.2f},{:.2f},{}".format(DayUp,DayDown,Ratio))


#4
N=input()
N=eval(N)
X=N//2+1
for i in range(X):
    Star=" "*(X-1)+"*"*(i*2+1)
    X=X-1
    print("{}".format(Star))
    
    
#5
mod="ABCDEFGHIJKLMNOPQRSTUVWXYZABC"
P=input()
P=P.upper()
Len=len(P)
for i in range(Len):
    Character=P[i]
    if Character in [" "]:
        print(" ",end="")
    else:
        Position=mod.find(Character)
        C=mod[Position+3]
        print(C.lower(),end="")



len("老师好")    
s="abcd1234"
print(s.find("cd"))    
    
100//3 
100/0.3
1.23e-4+5.67e+4j.imag
abs(3-4j)

'abcd'<'ad'

'abc'<'abcd'
''<'a'
'ABCD'>'abcd'
1.23e+4+9.87e+6j.imag





