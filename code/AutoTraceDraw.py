# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:54:24 2018

@author: QJ
"""

#AutoTraceDraw.py
import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals=[]
f = open("F:/zuoye/wanglab/课程\Python程序语言设计/第七周文件和数据格式化/data.txt")
for line in f:
    line = line.replace("\n","")  #去点换行符
    datals.append(list(map(eval,line.split(","))))   #以逗号为分隔符分割字符串，生成列表,map对每一个元素执行第一个参数(eval)对应的函数
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()