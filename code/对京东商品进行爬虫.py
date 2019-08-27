# -*- coding: utf-8 -*-
"""
Created on Wed May  2 21:52:13 2018

@author: QJ
"""

import requests
r = requests.get("https://item.jd.com/2967929.html")
r.status_code
r.encoding
r.text[:1000]


#全代码
import requests
url = "https://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")