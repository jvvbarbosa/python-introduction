#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:32:10 2019

@author: trn2503
"""


a = []

if a:
    print('Yes')
else:
    print('Nope!')
    
# While loops    
epsilon = 1.0
while 1 + epsilon > 1:
    epsilon /= 2
    print(epsilon)

for c in 'hello world':
    print(c)




for index, item in enumerate('my data'):
    print(item, 'was in position', index)
    
    
    
def my_enumerate(it):
    index_l = list(range(len(it)))
    return zip(index_l, it);


for index, item in my_enumerate('my data'):
    print(item, 'was in position', index)