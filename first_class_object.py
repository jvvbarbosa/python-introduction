#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:27:52 2019

@author: trn2503
"""

import math
trig = math.sin, math.cos, math.tan
for fn in trig:
    print(fn, fn(math.pi/3))