#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:52:45 2019

@author: trn2503
"""
from functools import partial
from operator import itemgetter

def get_first_element(entry):
    return entry[0]

def get_second_element(entry):
    return entry[1]


def key_factory(n):
    """
    Currying is what we are doing here
    writing a two parameter function and 
    representing them as a chain of 2 functions
    so we can feed the parameters at any point in time
    """    
    def key_giver(entry):
        return entry[n]

    return key_giver

def key(n, pair):
        return pair[n]


with open ('/etc/passwd', 'r') as file:
    users = []
    users_dict = {}
    for line in file:
        user_name, _, user_id, _ = line.split(':', 3)
        users.append((int(user_id), user_name))
        users_dict[int(user_id)]=user_name
    
#users.sort(key=key_factory(0)) #This is a very valid solution
#users.sort(key=partial(key, 0))
users.sort(key=itemgetter(0)) #We can use an already existing function
users.sort(key=(lambda pair:pair[0]))
user_dict_items = sorted(users_dict.items())
print('Sorted list:\n')
for uid, uname in users:
    print(uid, uname)
    

#print('Sorted dictionary items:\n', user_dict_items, '\n')
#in the definition of sort, the lonely * means that
#any further arguments passed must be keyword arguments

#In the definition of sort, / means that any previous 
#arguments must be bound to positional arguments

#for instance it is impossible to say sort(iterable = something)
#it has to be sort(something)
    
#Advantages of dictionaries
#   1 - Associative DS (data structure)
#   2 - FAST RAL(random access lookup) O(1)
#   3 - No order (good for data that doesnt have an intuitive order)
    
    
#Disadvantages of Dictionaries
#   1 - Memory overhead
#   2 - No lookup from value to key
#   3 - No order (if order matters)
