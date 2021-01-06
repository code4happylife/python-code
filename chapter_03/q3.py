#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q3.py
@time: 2021/1/6 10:57 上午
@desc:
'''

num_input = int(input("Give me a number :"))
result = dict()

for i in range(1, num_input+1):
    result[i] = i*i


print(result)




