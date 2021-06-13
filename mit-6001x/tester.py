#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:58:41 2021

@author: satheesh
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    a = ''.join(sorted(aStr))
    
    low = 0
    high = len(a)
    mid = (low+high)/2
    
    while mid != low:
        if char < a[mid]:
            low = mid
        else:
            high = mid
        mid = (low+high)/2
    
    return 
    
    