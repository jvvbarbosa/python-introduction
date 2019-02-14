#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:14:05 2019

@author: trn2503
"""

#When a class is called (instantiated)
#__new__ is called __new__( , *arguments in the call)
#self is the output of __new__
#__init__ gets the instance created by __new__ and the other arguments in the class call
#__init__ modifies this instance in what way necessary and that instance is returned by the class call
class Counter:

    def __init__(self, start):
        self.count = start

    def up(self, n=1):
        self.count += n

    def down(self, n=1):
        self.count -= n
        
class AddCounter(Counter):
    
    def __repr__(self):
        return 'AddCounter({.count})'.format(self)
    
    def __str__(self):
        return '{.count}'.format(self)
    
    def __add__(self, other):
        return AddCounter(self.count+other.count)
    
    __radd__ = __add__