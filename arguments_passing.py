#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:29:54 2019

@author: trn2503
"""


def one(a, b, *args):
    """ 
    Collect all remaining positional arguments into a tuple
    and bind it to the name which follows the * (args in this case)
    """    
    return args;

#The * here means: take this container of data
# and expand it into positional arguments
#Same as writing one('h', 'e', 'l', 'l', 'o')
one(*'hello') 
one(*range(6))

def two(a = 1, b = 2):
    
    return a, b

two()
two(9, 8)
two(b=8)

#Similarly here we are unpacking the dictionary
#into keyoword arguments by using the ** in the
#argument passing
two(**{'b':'banana', 'a':'apple'})

def three(*args, **kwds):
    """ 
    Collect all remaining keyword arguments into a dictionary
    and bind it to the name which follows the ** (kwds in this case)
    """    
    return args, kwds
  
three()
three(8)
three(8, dir)
three(8, dir, b=10)
three(8, dir, b=10, a=3)
#three(b=dir, 10) #Syntax Error because positional arguments come after keyword arguments
three(c=8, a=2, b=dir, args=7)#args will be put into the dictionary and not setting the argument args to 7



def four(a,b=1, *args, **kwds):
    return a, b, args, kwds

a,b,c = 1,2,3
a,b,*rest='thisandthat'
a,b,*rest, x,y,z = 'thisandthat'
  
    
