#!/usr/bin/env python
# encoding: utf-8
'''
@author: developer
@contact:
@software:
@file: q7.py
@time: 2021/1/11 10:45 上午
@desc:
'''



'''
Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional 
array.
 The element value in the i-th row and j-th column of the array should be i*j. 
 Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to 
 the program: 3,5 Then, 
 the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints: Note: In case of input data being supplied to the question, 
it should be assumed to be a console input in a comma-separated form.

'''

line_row = [x for x in input("Please input two numbers:").split(',')]
line = int(line_row[0])
row = int(line_row[1])
temp = []

for i in range(line):
    temp.append([0]*row)

for i in range(line):
    for j in range(row):
        temp[i][j] = i*j

print(temp)


