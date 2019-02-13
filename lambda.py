#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:48:04 2019

@author: trn2503
"""

from functools import reduce
from operator import add
from operator import mul

lambda a,b,c: a*b+c
(lambda a,b,c: a*b+c)(2,3,4)
lambda a,b,c: a*b+c(2,3,4)
(lambda a,b,c: a*b+c(2, 3, 4))(10, 20, lambda x, y, z: x*y*z)
(lambda a,b,c: a*b+c(2, 3, 4))([10, 20], 3, lambda x, y, z: [x*y*z])
(lambda a,b,c: a*b+c(2, 3, 4))(['daisy', 'jon'], 3, lambda x, y, z: [x, y, z])


#maps the function to the iterables (one iterable per argument)
map(lambda a:a+1, [1,2,3,4]) 

#recreating zip with map
tuple(map(lambda *args:args, 'apple', 'banana', 'orange'))

#Filters out the ones that have a remainder of 0
list(filter(lambda x:x%2, range(20)))

#Applies the function in sequence
reduce(lambda a, b:a+b, range(10))
reduce(add, range(10))

#Calculation a factorial of 100
reduce(mul, range(1, 101))
reduce(lambda a,b:a*b, range(1, 101))
