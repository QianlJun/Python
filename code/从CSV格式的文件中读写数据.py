# -*- coding: utf-8 -*-
"""
Created on Wed May  2 16:53:31 2018

@author: QJ
"""

#从CSV格式的文件中读取数据
fo = open(fname)
ls = []
for line in fo:
    line = line.replace("\n","")  #去掉换行符
    ls.append(line.split(","))    #ls
fo.close()


#将数据写入CSV格式的文件
ls= [[],[],[]]  #二维列表
f = open(fname,"w")
for item in ls:
    f.write(",".join(item) + '\n')
f.close

#二位数据的逐一处理
ls = [[],[],[]] #二维列表
for row in ls:
    for column in row:
        print(ls[row][column])