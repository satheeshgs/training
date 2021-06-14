from math import tan, pi

def polySum(n, s):
    '''
    input: n (number of sides of polygon), s (length of each side)
    returns: sum of the area plus the square of the perimeter of the polygon to 4 decimal places
    '''
    def areaPoly(n, s):
        '''
        input: n (number of sides of polygon), s (length of each side)
        returns the area of the regular polygon
        '''
        return (0.25*n*s**2)/tan(pi/n)

    def periPoly(n, s):
        '''
        input: n (number of sides of polygon), s (length of each side)
        returns perimeter of the polygon
        '''
        return n*s

    polysum = areaPoly(n, s) + periPoly(n, s)**2
    return round(polysum, 4) #returning to 4 decimal places
