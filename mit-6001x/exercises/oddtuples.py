#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:31:44 2021

@author: satheesh
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    aTup_odd = ()
    for i in range(0,len(aTup),2):
        aTup_odd += (aTup[i],)
    
    return aTup_odd
    