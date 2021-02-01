#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q15.py
@time: 2021/2/1 9:36 上午
@desc:
'''

'''
Level 2

Question: Write a program that computes the value of a+aa+aaa+aaaa 
with a given digit as the value of a. 
Suppose the following input is supplied to the program: 9 Then, 
the output should be: 11106

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.

'''

digit = input("Give me a digit:")

digit_1 = int(digit)
digit_2 = digit_1 * 10 + digit_1
digit_3 = digit_2 * 10 + digit_1
digit_4 = digit_3 * 10 + digit_1
result = digit_1 + digit_2 + digit_3 + digit_4
print(result)


