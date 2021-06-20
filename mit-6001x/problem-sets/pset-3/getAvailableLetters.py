#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 00:24:47 2021

@author: satheesh
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join(char for char in 'abcdefghijklmnopqrstuvwxyz' if char not in lettersGuessed)