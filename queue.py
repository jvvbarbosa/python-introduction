#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:43:52 2019

@author: trn2503
"""

class QueueIsEmpty(Exception):
    pass


class Queue:
    
    def __init__(self):
        self._queue = []
        
    def add(self, item):
        self._queue.append(item)
        
    def pop(self):
        try:
            return self._queue.pop(0)
        except IndexError:
            raise QueueIsEmpty('There are no elements in the queue')
            
            
            
class EmergencyQueue(Queue):
    
    def push(self, item):
        self.queue.insert(0, item)
        
class NoisyQueue(Queue):
    
    def __call__(self):
        print('I am an extremely noisy queue! WAAAAAAAA')
        
    def add(self, item):
        Queue.add(self, item)
        print('Added the following item to queue:', item)