# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:24:48 2018

@author: QJ
"""
import requests
r = requests.get("https://python123.io/ws/demo.html")
r.text
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")   #对demo的html的解析
print(soup.prettify())
soup.title   #获得标题
tag = soup.a   #获得a标签
tag
soup.a.name  #a标签的名字
soup.a.parent.name  #a标签的父标签的名字（包含a标签的标签）
soup.a.parent.parent.name  #a标签额父标签的父标签的名字
tag.attrs  #获得a标签的属性
tag.attrs['class']
tag.attrs['href'] #
type(tag.attrs)  #标签属性的类型
type(tag)   #标签的类型
soup.a.string  #a标签的字符串信息
soup.p
soup.p.string  #p标签的字符串信息
type(soup.p.string) #类型


newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>","html.parser")
newsoup.b.string             #！注释被去掉了
type(newsoup.b.string)   
newsoup.p.string
type(newsoup.p.string)

soup.head
soup.head.contents  #查看head节点的儿子节点
soup.body.contents  #body的儿子节点的
len(soup.body.contents)  #有多少儿子节点
soup.body.contents[1]  #返回第一个节点
for child in soup.body.children:    #遍历所有的儿儿子节点
    print(child)
for child in soup.body.descendants:  #遍历所有的子孙节点
    print(child)

soup.title.parent    #title标签的父亲
soup.html.parent   #html标签的父亲

#标签树的上行遍历
soup = BeautifulSoup(demo,"html.parser")
for parent in soup.a.parents:    #遍历a标签的所有先辈标签并打印名字，soup本身不存在name的信息
    if parent in None:
        print(parent)
    else:
        print(parent.name)
        
#标签树的平行遍历
soup.a.next_sibling  #a标签的下一个平行节点的标签
soup.a.next._sibling.bet_sibling
soup.a.previous_sibling  #a标签的上一个平行节点的标签

for sibling in soup.a.next_siblings:   #遍历后续节点
    print(sibling)     
for sibling in soup.a.previous_siblings:  #遍历前续节点
    print(sibling)

#让html页面的显示更加友好prettify
soup.prettify()
print(soup.prettify())
print(soup.a.prettify())


































