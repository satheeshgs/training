#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:55:39 2021

@author: satheesh
"""

def palindrome(s):
    '''input a string and check if its a palindrome'''
    def toChars(s):
        '''convert to characters; remove punctuations'''
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans +=c 
        return ans
    
    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))