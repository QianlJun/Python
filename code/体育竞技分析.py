# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:46:08 2018

@author: QJ
"""

import random as r
def printIntro():     #说明函数的作用
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)")
def getInputs():      #获得用户的输入
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的场次: "))
    return a,b,n
def printSummary(winsA,winsB):   #打印结果
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))
def simNGames(n,probA,probB):     #模拟n场比赛
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)   #模拟一次的函数
        if scoreA > scoreB:
            winsA +=1
        else:
            winsB +=1
    return winsA,winsB
def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = "A"
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if r.random() < probA:      #产生随机数，比A小就认为A赢
                scoreA +=1
            else:
                serving = "B"
        else:
            if r.random() < probB:
                scoreB +=1
            else:
                serving = "A"
    return scoreA,scoreB
def gameOver(a,b):   #结束的条件
    return a==15 or b ==15
def main():
    printIntro()
    probA,probB,n= getInputs()
    winsA,winsB = simNGames(n,probA,probB)
    printSummary(winsA,winsB)
main()


































