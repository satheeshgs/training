#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 20:14:55 2021

@author: satheesh
"""

def fib_loop(n):
    '''Returns Fibonacci number for the integer argument n.
    Uses loop from 1 to n.'''
    if n < 1:  return None
    if n == 1:   return 1
    elif n == 2: return 2
    val = [1,2]     # List of fib values for numbers 1 and 2
    for i in range(3, n+1):
        val[(i+1)%2] = sum(val)
    return max(val)