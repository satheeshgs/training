def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    aStr = ''.join(sorted(aStr))
    if len(aStr) == '0':
        return False

    if len(aStr) == 1:
        return char == aStr[0]

    mid = len(aStr)//2
    if char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    else:
        return isIn(char, aStr[mid:])


print(isIn('a', 'lingarajapuram'))
