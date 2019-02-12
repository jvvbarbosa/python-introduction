#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:56:47 2019

@author: trn2503
"""

def make_adder(n):

    def adder(x):
        return n+x

    return adder
    

add3 = make_adder(3)
add9 = make_adder(9)
print(add3(4), add9(4))
  