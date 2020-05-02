# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:02:56 2019

@author: Mr.Zhang
"""

#关系运算符
print(1<2<3)
print(1<2>3)
print(1<3>2)
#if a = 3: 错误，不允许使用赋值运算符“=”
#if (a=3) and (b=4):`
print(1>2>xxx) #惰性求值，只计算必须计算的值
print(3 and 5)
print(3 or 5)
print(0 and 5)
print(0 or 5)
print(not 3)
print(not 0)

def Join(chList, sep = None):
    return (sep or ",").join(chList)
chTest = ['1', '2', '3', '4', '5']
print(Join(chTest))
#也可以：
def Join2(chList, sep = ','):
    return sep.join(chList)
print(Join2(chTest))