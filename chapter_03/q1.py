#!/usr/bin/env python
# encoding: utf-8
'''
@author: developer
@contact:
@software:
@file: q1.py
@time: 2021/1/4 5:59 下午
@desc:
'''

result = []
for num in range(2000, 3201):
    if (num % 7 == 0) and (num % 5 != 0):
        result.append(str(num))

print(','.join(result))



