#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:07:15 2017

@author: yezi
"""

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import re
d = path.dirname('/Users/yezi/Desktop/temp/pypypy/')
text = open(path.join(d,'cellword.txt')).read()
pattern = '[' + "\'" +']'
text = re.sub(pattern,'',text)
#text = open('/Users/yezi/Desktop/未命名文件夹/pypypy/alice.txt','r').read()
alice_coloring = imread(path.join(d, "tree.png"))
wc = WordCloud(background_color="white",max_words=5000,mask=alice_coloring,max_font_size=70,
               random_state=2000,width=1800,height=800)
wc.generate(text)
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(wc)
plt.axis("off")
plt.figure()
#plt.imshow(wc.recolor(color_func=image_colors))
#plt.axis("off")
plt.figure()
#plt.imshow(alice_coloring, cmap=plt.cm.gray)
#plt.axis("off")
wc.to_file(path.join(d, "1.png"))