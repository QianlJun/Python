# -*- coding: utf-8 -*-
"""
Created on Thu May  3 21:52:35 2018

@author: QJ
"""


import requests
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
demo
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):    #查找a标签
    print(link.get('href'))      #找到的a标签的额属性href

soup.find_all('a')   #查找所有的a标签
soup.find_all(['a','b'])   #查找所有的a,b标签

for tag in soup.find_all(True):  #找到所有的标签名称
    print(tag.name)
    
import re    #正则表达式库
for tag in soup.find_all(re.compile('b')):    #返回以b开头的所有标签
    print(tag.name)

soup.find_all('p','course')  #返回p标签的带course的标签
soup.find_all(id='link1')   #返回id=link1的标签


import re
soup.find_all(id=re.compile('link'))   #输出以link开头的标签信息

soup.find_all('a')
soup.find_all('a',recursive=False)    #recursive是否对子孙进行查找,mo

soup.find_all(string = "Basic Python")
import re
soup.find_all(string = re.compile("python"))  #检索所有出现python的字符创



























