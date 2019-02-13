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
        print(reduce(add, map(float, line.split(' '))))


        
            