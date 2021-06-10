def bunny_id(x,y):
    id = 1
    for i in range(1,y): #moving to the starting point of the necesary floor
        id +=i
    for j in range(1,x): #traversing through the floor
        id +=(y+j)
    return str(id)


def test_bunny_id1():
    assert bunny_id(5,10) == str(96)


def test_bunny_id2():
    assert bunny_id(1, 1) == str(1)


def test_bunny_id3():
    assert bunny_id(3,2) == str(9)


def test_bunny_id4():
    assert bunny_id(2, 3) == str(8)