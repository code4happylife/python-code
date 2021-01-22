#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q13.py
@time: 2021/1/21 8:46 下午
@desc:
'''


'''
Question 13
Level 2

Question: Write a program that accepts a sentence and calculate the number of 
letters and digits. Suppose the following input is supplied to the program: hello world! 
123 Then, the output should be: LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.

Solution:
'''


input_content = input()

char_num = 0
digit_num = 0

for item in input_content[:]:
    if '0' < item < '9':
        digit_num += 1
    elif 'a' < item.lower() < 'z':
        char_num += 1
    else:
        pass

print("LETTERS "+str(char_num)+" DIGITS "+str(digit_num))





