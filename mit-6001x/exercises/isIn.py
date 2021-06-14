# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 18:17:06 2021

@author: satheeshgs
"""
import math

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here    
    def sortAlpha(s):
        '''
        input: alphabetical string
        returns: sorted alphabetical string
        '''
        return ''.join(sorted(s))
    
    s = sortAlpha(aStr)
    low = 0
    high = len(s)
    mid = math.floor((low+high)/2)

    while mid != low and mid!=high:
        if char < s[mid]:
            low = mid
        elif char > s[mid]:
            high = mid
        else:
            return True
        
        mid = math.floor((low+high)/2)
    
    return False

print(isIn('a', 'abc'))