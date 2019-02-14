#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:19:20 2019

@author: trn2503
"""





def gen_ints(start, stop):
    print('hello from gen_ints')
    while start < stop:
        yield start       # next(...)
        start += 1
    return                # StopIteration


def fibg(): #This contains all the fibbonaci numbers to infinity
    yield 0
    current, next = 0, 1
    
    while True:
        current, next = next, current + next
        yield current




def genumerate(iterable, start=0):
    count = start;
    for item in iterable:
        yield count, item
        count +=1



def my_enumeratez(it, start=0):
    return zip(range(start, start+len(it)), it);#this does not work with iterables because of len

from itertools import count
def ienumerate(iterable, start = 0):
    return zip(count(start), iterable); #This is genuinely lazy