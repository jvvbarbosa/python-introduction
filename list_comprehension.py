#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:33:06 2019

@author: trn2503
"""

a = list(map(lambda x:x*x, range(10)))
print(a)
#Equivalent
a = [ x*x for x in range(10) ]
print(a)
