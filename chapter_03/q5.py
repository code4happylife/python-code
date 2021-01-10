#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/1/10 18:34
#@Author: developer
#@File  : q5.py

'''

Question: Define a class which has at least two methods: getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints: Use init method to construct some parameters
'''


class StringTest():
    def __init__(self):
        self.teststring = ''

    def getString(self):
        self.teststring = input("Please input a string:")

    def printString(self):
        print(self.teststring.upper())



string_object = StringTest()
string_object.getString()
string_object.printString()

