# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:00:27 2018

@author: QJ
"""

fo = open("output.txt","w+")
ls = ["中国","法国","美国"]
fo.writelines(ls)
fo.seek(0)       #指针回到文件开始
for line in fo :
    print(line)
fo.close()