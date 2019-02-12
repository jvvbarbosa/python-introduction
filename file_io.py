#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:40:46 2019

@author: trn2503
"""

file = open('myfile', 'w')
print(1, 2, 3, 4, file=file)
file.write('5 6 7 8')
file = open('myfile', 'r')
for line in file:
    print(line)

#The context manager with run the closing code
#In this case it is the close()
with open('myfile', 'w') as file:
    print(1, 2, 3, 4, file=file)
    file.write('5 6 7 8')
with open ('myfile', 'r') as file:
    for line in file:
        print(line)