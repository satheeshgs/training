#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:58:41 2021

@author: satheesh
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test_val = b
    while a%test_val!=0 or b%test_val !=0:
        test_val-=1
    return test_val