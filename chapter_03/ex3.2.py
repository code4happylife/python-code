#!/usr/bin/env python
# encoding: utf-8
'''
@author: developer
@contact:
@software:
@file: ex3.2.py
@time: 2020/11/25 9:44 上午
@desc:
'''

names = ['zhangsan', 'lisi', 'jack']

message = []

for name in names:
    message.append('Hi ! ' + name.title() + ' ,Have a nice day today ! ')

print(message[0])
print(message[1])
print(message[2])
