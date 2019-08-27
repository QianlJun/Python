# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:53:33 2018

@author: QJ
"""

import requests
url = "http://m.ip138.com/ip.asp?ip=+"      #ip138的API
try：
    r = requests.get(url+'60.206.78.86')   #要查询的ip地址
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])   #限制输出的文本量
except:
    print("爬取失败")
    


