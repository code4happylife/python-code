#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q10.py
@time: 2021/1/14 4:28 下午
@desc:
'''


'''
Question 10
Level 2

Question: Write a program that accepts a sequence of whitespace separated words as input and prints 
the words after removing all duplicate words and sorting them alphanumerically. 
Suppose the following input is supplied to the program: 
hello world and practice makes perfect and hello world again Then, 
the output should be: again and hello makes perfect practice world

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input. 
We use set container to remove duplicated data automatically and then use sorted() to sort the data.


'''

input_content = input()
origin_input = input_content.split(' ')
set_of_input = set(origin_input)
print(' '.join(sorted(set_of_input)))




