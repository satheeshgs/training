#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 21:49:58 2021

@author: satheesh
"""

s = 'azcbobobegghakl'

#bob_count 
bob_count = 0

for i in range(len(s)+1):
    if s[i:i+3] == 'bob':
        bob_count +=1

print('Number of times bob occurs is: ' + str(bob_count))


#alphabetical order

current_long = ''
maximum_length = ''

for i in range(len(s)-1):
    if len(current_long) ==0:
        current_long = current_long + s[i]
    if s[i] <= s[i+1]:
        current_long = current_long + s[i+1]
    elif len(maximum_length) < len(current_long):
        maximum_length = current_long

print(maximum_length)
    


