#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q14.py
@time: 2021/1/22 7:22 下午
@desc:
'''


'''
Level 2

Question: Write a program that accepts a sentence and calculate the number of upper case letters 
and lower case letters. 
Suppose the following input is supplied to the program: Hello world! 
Then, the output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.

'''
sentence = input("Please input a sentence:")
upper = 0
lower = 0

for ch in sentence:
    if 'A' < ch < 'Z':
        upper = upper + 1
    elif 'a' < ch < 'z':
        lower = lower + 1
    else:
        pass

print("UPPER CASE ", str(upper), "LOWER CASE ", str(lower))




