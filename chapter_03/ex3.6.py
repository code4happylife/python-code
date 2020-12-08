#!/usr/bin/env python
# encoding: utf-8
'''
@author: developer
@contact:
@software:
@file: ex3.6.py
@time: 2020/12/2 9:42 上午
@desc:
'''

"""
for bigger table
"""

friends = ['a', 'b', 'c']

friends.insert(0, 'd')
friends.insert(2, 'e')
friends.append('f')
print("Find a bigger table.")
for friend in friends:
    print("Thanks a lot "+friend.title()+" ! For joining us to enjoy tonight's party.")

print(friends)
del friends[0]
del friends[1]
print(friends)


