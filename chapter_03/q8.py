#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q8.py
@time: 2021/1/12 10:18 上午
@desc:
'''

'''
Level 2

Question: Write a program that accepts a comma separated sequence of words as input 
and prints the words in a comma-separated sequence after sorting them alphabetically. 
Suppose the following input is supplied to the program: without,hello,bag,world Then, 
the output should be: bag,hello,without,world

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.


'''

words_list = [x for x in input("Please input a few words:").split(',')]

words_list.sort()
print(','.join(words_list))

