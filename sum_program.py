#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 13:27:18 2019

@author: trn2503
"""
from operator import add
from functools import reduce


def is_float(token):
    try:
        float(token)
       
    except ValueError:
        return False
    else:
        return True

def my_float(f):
    try:
        return float(f)
    except ValueError:
        return 0.0

with open ('numbers.txt', 'r') as file:
    for line in file:
            #print(sum(map(float, filter(isfloat, line.split()))))
            tokens = line.split()
            valid_tokens = filter(is_float, tokens)
            numbers = map(float, valid_tokens)
            print(sum(numbers))
            #print(sum(map(float, filter(my_float, line.split())))) #All in one line
        #print(reduce(add, map(float, line.split()), 0)) #Optional initial value for reduce handles empty line


        
        
            