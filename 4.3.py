# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:50:29 2019

@author: Mr.Zhang
"""

a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
for i, v in enumerate(a_list):
    print('列表第{0}个元素是{1}'.format(i, v))


for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
        
for i in range(1, 10):
    for j in range(1, i+1):
        print('{0} * {1} = {2}'.format(i, j , i*j), end = '')
    print()

s = 0
for i in range(1, 101):
    s+=1
else:
    print(s)

sum(range(1, 101))

for n in range(100, 1, -1):
    if n % 2 == 0:
        continue
    for i in range(3, int (n**0.5)+1, 2):
        if n % i == 0:
            break
    else:   #当for循环自然结束时执行else
        print(n)
        break
    

digits = (1, 2, 3, 4)

result = []
import time
before = time.time()

for i in range(10000):
    for i in digits:
        for j in digits:
            for k in digits:
                result.append(i*100 + j * 10 + k)
print("时间",time.time()-before);                
   
before = time.time()

for i in range(10000):
    for i in digits:
        i = i*100
        for j in digits:
            j = j * 10
            for k in digits:
                result.append(i + j + k)
print("时间",time.time()-before);         

#将模块中的方法转换成局部变量提高运行速度
before = time.time()
import math
for i in range(1000000):
    math.sin(i)
print("时间",time.time()-before);  

before = time.time()
loc_sin = math.sin
for i in range(1000000):
    loc_sin(i)
print("时间",time.time()-before);  
