#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q4.py
@time: 2021/1/7 9:34 上午
@desc:
'''

num_string_input = input("Please input a sequence of numbers separated by comma please:")
list_output = []
for num in num_string_input.split(','):
    list_output.append(num)

print(list_output)

tuple_output = tuple(list_output)
print(tuple_output)




