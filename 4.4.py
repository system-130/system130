# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:36:11 2019

@author: Mr.Zhang
"""

numbers = []
while True：:
    x = input('请输入一个成绩：'):
    try:
        numbers.append(float(x))
    except:
        print "成绩不合法！"
    while True:
        flag = input("继续输入吗（yes/no）")
        if flag.lower() not in ('yes', 'no'):
            print('只能输入yes或no')
        else break
    if flag.lower() == 'no':
        break

print(sum(numbers)/len(numbers))