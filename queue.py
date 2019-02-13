#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:43:52 2019

@author: trn2503
"""

class Queue:
    
    def __init__(self):
        self.queue = []
        
    def add(self, item):
        self.queue.append(item)
        
    def pop(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            raise