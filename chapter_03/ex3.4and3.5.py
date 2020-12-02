#!/usr/bin/env python
# encoding: utf-8
'''
@author: developer
@contact:
@software:
@file: ex3.4and3.5.py
@time: 2020/12/2 9:34 上午
@desc:
'''


friends = ['a', 'b', 'c']
print("I'd like to invite "+friends[0]+" to this party tonight.")
print("I'd like to invite "+friends[1]+" to this party tonight.")
print("I'd like to invite "+friends[2]+" to this party tonight.")

no_time_friend = friends.pop(2)
print("But "+no_time_friend+" may have no time to participate this party.")
friends.append('d')
print("So I may have to invite "+friends[2]+" to enjoy this party.")

for f in friends:
    print("********")
    print("Finally, I am very happy to tell you that "+f+" will definitely join us for this party .")

