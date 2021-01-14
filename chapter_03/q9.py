#!/usr/bin/env python
# encoding: utf-8
'''
@author:
@contact:
@software:
@file: q9.py
@time: 2021/1/12 8:41 下午
@desc:
'''

'''
Question 9
Level 2

Write a program that accepts sequence of lines as input and prints the lines 
after making all characters in the sentence capitalized. 
Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, 
the output should be: HELLO WORLD PRACTICE MAKES PERFECT

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

'''

lines = []
while True:
    try:
        line = input("Please input multiple lines:")
    except EOFError:
        break
    lines.append(line)


result = ' '.join(lines)
print(result.upper())

# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break
#
# for sentence in lines:
#     print(sentence)

