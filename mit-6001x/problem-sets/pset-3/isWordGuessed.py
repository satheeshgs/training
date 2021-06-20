#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 22:14:08 2021

@author: satheesh
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    # if len(secretWord) == 1:
    #     return secretWord[0] in lettersGuessed
    # else:
    # for i in range(len(secretWord)):
    #     if secretWord[i] not in lettersGuessed:
    #         return False
    # return True
    return set(secretWord) <= set(lettersGuessed)