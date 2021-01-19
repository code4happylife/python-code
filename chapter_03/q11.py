#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q11.py
@time: 2021/1/15 6:06 下午
@desc:
'''



'''
Question 11
Level 2

Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as 
its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
 Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

'''


input_digits = [x for x in input().split(',')]

number_list = []
for each_num in input_digits:
    number_list.append(int(each_num, 2))

result = []

for i in range(len(number_list)):
    if number_list[i] % 5 == 0:
        result.append(input_digits[i])


print(''.join(result))

