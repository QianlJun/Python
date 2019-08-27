# -*- coding: utf-8 -*-
"""
Created on Wed May  2 20:21:01 2018

@author: QJ
"""

import requests
r = requests.get("http://www.baidu.com")
r.status_code
r.encoding
r.apparent_encoding
r.encoding = 'utf-8'
r.text


#爬取网页的通用代码框架
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__ == "__main__":
    url ="http://www.baidu.com"
    print(getHTMLText(url))