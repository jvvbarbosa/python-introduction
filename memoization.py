#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:51:45 2019

@author: trn2503
"""

from time import time as timer

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n - 2) 

#fib(36) takes 4 seconds to run
#it would be cool to cache a call
#We write a memorizer cabaple of storing answers from a func
#This memorizer returns a better version of a func that caches its own results

def memo(fn):
    cache = {}
    def proxy(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return proxy

def time(func, *args, **kwds):
    start = timer()
    res = func(*args, **kwds)
    stop = timer()
    return res, stop - start


#Input is a lambda
#timel(lambda: fib(36))
def timel(tunk):
    start = timer()
    res = tunk()
    stop = timer()
    return res, stop - start
    