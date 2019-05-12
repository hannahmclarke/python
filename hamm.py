# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:54:43 2019

@author: Hannah
"""

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

def mutation (s,t):
    dh = 0  
    for i in range(0, len(s)):
        if s[i] != t[i]:
            dh = dh + 1
    print (dh)

mutation (s,t)
     