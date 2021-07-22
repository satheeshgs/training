def corners(height, width):
    for i in range(0, 2):
        for j in range(0, 2):
            print(i, j)
    
    print('left top')

    for i in range(height-1, height-3, -1):
        for j in range(width-1, width-3, -1):
            print(i, j)
    
    print('right bottom')

    for i in range(0, 2):
        for j in range(width-1, width-3, -1):
            print(i,j)
    
    print('left bottom')
    
    for i in range(height-1, height-3, -1):
        for j in range(0, 2):
            print(i,j)
    
    print('right top')


def first_row(height, width):
    print('first row')
    for i in range(1, width-1):
        counter = 0
        j = 0
        for k in range(-1, 2):
            for l in range(0,2):
                print(i+k, j+l)
                counter+=1
        print('--------Counter = ', counter)

def last_row(height, width):
    print('last row')
    for i in range(1, width-1):
        counter = 0
        j = height - 1
        for k in range(-1, 2):
            for l in range(-1, 1):
                print(i+k, j+l)
                counter+=1
        print('--------Counter = ', counter)

def left_column(height, width):
    print('left column')
    for j in range (1, height-1):
        counter = 0
        i = 0
        for k in range(0,2):
            for l in range(-1,2):
                print(i+k, j+l)
                counter+=1
        print('--------Counter = ', counter)

def right_column(height, width):
    print('right column')
    for j in range (1, height-1):
        counter = 0
        i = width - 1
        for k in range(-1,1):
            for l in range(-1,2):
                print(i+k, j+l)
                counter+=1
        print('--------Counter = ', counter)


first_row(4,4)
last_row(4,4)
left_column(4,4)
right_column(4,4)
