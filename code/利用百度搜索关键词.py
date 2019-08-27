# -*- coding: utf-8 -*-
"""
Created on Wed May  2 22:15:49 2018

@author: QJ
"""

import requests
kv = {'wd':'Python'}   #接口
r = requests.get("http://www.baidu.com/s",params = kv)  #params添加字段
r.status_code
r.request.url
len(r.text)

#百度搜索全代码
keyword = "Python"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
    
    