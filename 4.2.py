# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:10:44 2019

@author: Mr.Zhang
"""

#选择结构


'''
#单分支选择结构
x = input('input two numbers:')
a,b = map(int, x.split())
if(a>b):
    a, b = b, a
print(a, b)
'''

'''
if 3 > 2: print('ok')
if True: print(3);print(5)
jitu, tui = map(int , input('请输入鸡兔总数和腿的总数：').split())
tu = (tui - jitu*2)/2
if int(tu) == tu:
    print('鸡：{0}, 兔:{1}'.format(int (jitu-tu), int(tu)))
else:
    print('数据不正确，无解')
'''
    
##三元运算符
#value1 if condiction else value2
a = 5
print(6) if a > 3 else print(5)

print(6 if a > 3 else 5)

b = 6 if a>13 else 9
print(b)

import math
x = math.sqrt(9) if 5 > 3 else random.randint(1, 100)
print(x)

'''
三元运算符可以嵌套使用实现复杂的多分支选择结构的效果，但是这样的代码可读性非常差，不建议使用。
'''

x = 3
f = lambda x : x * x
print((1 if x > 2 else 0) if f(x) > 5 else ('a' if x < 5 else 'b'))

def func(score):
    if score>100 or score < 0:
        return 'wrong score.must between 0 and 100.'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'
print(func(67))

##选择结构的嵌套

def func(score):
    degree = 'DCBAAE'
    if score > 100or score < 0:
        return 'wrong.socore must between 0 and 100.'
    else:
        index = (score - 60) ##10
        if index >= 0:
            return degree[index]
        else:
            return degree[-1]
