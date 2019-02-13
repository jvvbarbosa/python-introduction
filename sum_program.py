#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 13:27:18 2019

@author: trn2503
"""
from operator import add
from functools import reduce

with open ('numbers.txt', 'r') as file:
    for line in file:
        #print(sum(map(float, line.split())))
        print(reduce(add, map(float, line.split()), 0)) #Optional initial value for reduce adds support for empty line


        
        
            