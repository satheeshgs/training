#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:32:58 2021

@author: satheesh
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    aDict_lengths = {}
    for key in aDict:
        aDict_lengths[key] = len(aDict[key])

    max_val = max(aDict_lengths.values()) #finding the maximum value
    
    for key in aDict_lengths:
        if aDict_lengths[key] == max_val:
            return key #returning the first key which corresponds to the maximum value