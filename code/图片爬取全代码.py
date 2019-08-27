# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:36:12 2018

@author: QJ
"""


import requests
import os
url = ""    #图片地址
root = ""   #保存目录
path = root +url.split('/')[-1]  #截取图片名称，保存
try：
    if not os.path.exists(root):   #判断根目录是否存在，如果不存在，就创建
        os.mkdir(root)
    if not os.path.exists(path):   #查看文件是否存在
        r = requests.get(url)
        with open(path,"wb") as:     #以二进制打开文件并保存
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")






























