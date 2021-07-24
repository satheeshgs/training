def corners(height, width):
    for i in range(0, height, height - 1):
        for j in range(0, width, width - 1):
            if i == 0 and j  ==0:
                print('left top')
                for k in range(0,2):
                    for l in range(0,2):
                        print(i+k, j+l)
         
            if i == height -1 and j ==0:
                print('left bottom')
                for k in range(-1, 1):
                    for l in range(0, 2):
                        print(i+k, j+l)

            if i == 0 and j == width -1:
                print('right top')
                for k in range(0,2):
                    for l in range(-1,1):
                        print(i+k, j+l)

            if i == height - 1 and j == width - 1:
                print('right bottom')
                for k in range(-1,1):
                    for l in range(-1,1):
                        print(i+k, j+l)
    

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



corners(5,4)
