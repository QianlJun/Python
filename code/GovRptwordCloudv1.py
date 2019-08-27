# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:53:19 2018

@author: QJ
"""

#GovRptwordCloudv1.py
import jieba
import wordcloud
f = open("F:\zuoye\wanglab\课程\Python程序语言设计\第七周文件和数据格式化\新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path = "msyh.ttc", \
                       width = 1000,height = 700,background_color = "white", \
                       max_words = 15)   #限制最多15个单词
w.generate(txt)
w.to_file("F:\zuoye\wanglab\课程\Python程序语言设计\第七周文件和数据格式化\output.png")

#生成的为五角星的词云
from scipy.misc import imread
mask = imread("fivestart.png")
w = wordcloud.WordCloud(font_path = "msyh.ttc", \
                       width = 1000,height = 700,background_color = "white", \
                       max_words = 15,mask = mask ) 
















