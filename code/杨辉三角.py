# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:43:27 2018

@author: QJ
"""

###杨辉三角函数yanghui()代码开始
def yanghui(n):
if not str(n).isdecimal() or n<2 or n>25:
    ##限制杨辉三角阶数，避免数字太大
    print('杨辉三角函数yanghui(n),参数n必须是不小于2且不大于25的正整数')
    return False
    #使用列表来生成杨辉三角
    x=[]
    for i in range(1,n+1):              ##生成初始的杨辉三角不规则举证
        x.append([1]*i)
    #计算杨辉三角矩阵其他值
    for i in range(2,n):
        for j in range(1,i):
            x[i][j]=x[i-1][j-1]+x[i-1][j]
    #输出杨辉三角
    for i in range(n):
        if n<=10:print(' '*(40-4*i),end='')
        for j in range(i+1):
            print('%-8d'%x[i][j],end='')
        print()
###杨辉三角函数yanghui()代码结束
    

###独立运行测试代码开始
if_name_='_main_':
    print('模块独立自运行测试输出： ')
    print('一、10阶杨辉三角如下： ')
    yanghui(10)