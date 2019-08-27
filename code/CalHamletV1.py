# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:39:51 2018

@author: QJ
"""

#CalHamletV1.py
def getText():
    txt = open("F:\zuoye\wanglab\课程\Python程序语言设计\hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{\}~':
        txt = txt.replace(ch," ")
    return txt
hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)   #对一个列表按照键值对的第二列从大到小排序
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
