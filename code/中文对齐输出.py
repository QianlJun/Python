# -*- coding: utf-8 -*-
"""
Created on Sat May  5 17:25:45 2018

@author: QJ
"""

#中文对齐输出,详键中国大学排名网络爬取
tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"     #采用中文空格chr(12288)填充，用于对齐
    print(tplt.format("排名","学校","总分",chr(12288)))   #对的表头的打印