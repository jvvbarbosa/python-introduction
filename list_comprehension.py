#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:33:06 2019

@author: trn2503
"""

#a = list(map(lambda x:x*x, range(10)))
#print(a)
#Equivalent
print('List comprehension example 1')
a = [ x*x for x in range(10) ]
print(a)



#Cartesian product
print('Another example, Cartesian product')
b = [ (x,y) for x in range(4) for y in 'abc' ]

print(b)

c = [ (x,y) for x in range(6) if x%2 for y in range(6) if x>y ]
print(c)
#Filter


#x = [A for b in B if C for d in D if E]

#x=[]
#for b in B:
#    if C:
#        for d in D:
#            if E:
#                x.append(A)


#Dictionary comprehension
{x:x*x for x in range(10)}

{x*x for x in range(10)}

#Lazy version of list comprehension -> Generators
a = (n*n for n in range(10))
next(a) 

sum(n*n for n in range(10))
