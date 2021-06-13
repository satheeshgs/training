#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:50:55 2021

@author: satheesh
"""

def fib_num(x):
    ''' x is int >=0
    returns fibonacci of x'''
    if x==0 or x ==1:
        return 1
    else:
        return fib_num(x-1)+fib_num(x-2)