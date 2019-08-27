# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:38:00 2018

@author: QJ
"""

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    return "" 

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:     #解析tbody标签的位置
        if isinstance(tr,bs4.element.Tag):     #找到的每所大学的tr标签，并的找到td标签
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
    

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"     #采用中文空格chr(12288)填充，用于对齐
    print(tplt.format("排名","学校","总分",chr(12288)))   #对的表头的打印
    for i in range(num):     #每所学校的信息打印出来,和表头相一致的格式
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
    print("Suc"+str(num))
    
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)   #top20的学校
main()





















    