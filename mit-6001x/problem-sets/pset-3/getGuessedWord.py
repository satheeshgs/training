#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:43:45 2021

@author: satheesh
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    # word =''
    # for i in range(len(secretWord)):
    #     if secretWord[i] not in lettersGuessed:
    #         word +='_'
    #     else:
    #         word +=secretWord[i]
    # return word
    return ''.join(char if char in lettersGuessed else '_' for char in secretWord)