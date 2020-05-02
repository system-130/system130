# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:30:05 2019

@author: Mr.Zhang
"""

d = dict(zip('1234','abcd'))
print(d)
x = input("please input a key\n")
print(d.get(x, "您输入的键不存在！"))