#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q2.py
@time: 2021/1/5 9:27 上午
@desc:
'''


def fact(num):
    if num == 0:
        return 1
    else:
        return fact(num-1)*num


test_num = int(input("Calculate the factorial of:"))
print("The factorial of test_num is", fact(test_num))

