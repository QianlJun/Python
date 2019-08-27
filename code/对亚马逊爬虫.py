# -*- coding: utf-8 -*-
"""
Created on Wed May  2 21:58:51 2018

@author: QJ
"""

#网站拒绝爬虫
import requests
r = requests.get("https://www.amazon.cn/gp/product/Bo1M8L5z3Y")
r.status_code
r.encoding
r.encoding = r.apparent_encoding
r.text
#查看发给亚马逊的头部用户信息
r.request.headers

#让程序模拟浏览器来访问
kv = {'user-agent':'Mozilla/5.0'}  #Mozilla是标准的浏览器识别字段
url = "https://www.amazon.cn/dp/B0057DJULK/ref=cngwdyfloorv2_recs_0?pf_rd_p=05f2b7d6-37ec-49bf-8fcf-5d2fec23a061&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=YA72MEKPAKDXETH4SGQ8&pf_rd_r=YA72MEKPAKDXETH4SGQ8&pf_rd_p=05f2b7d6-37ec-49bf-8fcf-5d2fec23a061"
r = requests.get(url,headers = kv)
r.status_code
r.request.headers

#全代码
import requests
url = ""
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)   #headers
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
    