# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:24:19 2019

@author: Mr.Zhang
"""
import random
x = [random.randint(0,100) for i in range(1000)]
print(x)
y = set(x)
for i in y:
    print(i,":",x.count(i))
