#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q12.py
@time: 2021/1/21 8:31 下午
@desc:
'''


'''
Question 12
Level 2

Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number. 
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.

'''
result = []
# int_temp = []
for num in range(1000, 3001, 1):
    str_num = str(num)
    # for item in str_num:
    #     int_temp.append(int(item))
    if int(str_num[0]) % 2 == 0 and int(str_num[1]) % 2 == 0 and int(str_num[2]) % 2 == 0 and int(str_num[3]) % 2 == 0:
        result.append(str_num)
    # int_temp = []

print(','.join(result))









