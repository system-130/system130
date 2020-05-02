# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:26:07 2019

@author: Mr.Zhang
"""

#示例1

import re

telNumber = ''' 
    Suppose my Phone No. is 0535-1234567,
    yours is 010-12345678,
    his is 025-87654321.
'''
pattern = re.compile(r'(\d{3,4})-(\d{7,8})')
print(telNumber)
index = 0
while True:
    matchResult = pattern.search(telNumber, index)
    if not matchResult:
        break
    print('-'*30)
    print('Success:')
    for i in range(3):
        print('Searched content:', matchResult.group(i),
              'Start form:', matchResult.start(i),'End at:',
              matchResult.end(i), 
              'Its span is:', matchResult.span(i))
    index = matchResult.end(2)
    
    
#示例2
    
import os
import re
def detectIframe(fn):
    content = []
    with open(fn, encoding = 'utf-8') as fp:
        for line in fp:
            content.append(line.strip())
    
    content = ' '.join(content)
    m = re.findall(r'<iframe\s+src=.*?></iframe>', content)
    if m:
        return {fn:m}
    return False

for fn in (f for f in os.listdir('.') if f.endswith(('.html', '.htm'))):
    r = detectIframe(fn)
    if not r:
        continue
    for k,v in r.items():
        print(k)
        for vv in v:
            print('\t', vv)




    