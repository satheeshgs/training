def solution(total_lambs):
    henchmen = stingy_lambs(total_lambs) - generous_lambs(total_lambs)
    return henchmen


def generous_lambs(total_lambs): #for the generous flow in the 2 to the power of n
    sum = 0
    while total_lambs > 2**sum:
        total_lambs -= 2**sum
        sum +=1
    return sum

def stingy_lambs(total_lambs): #for the stingy flow with a fibonacci series
    a = 0 
    b = 1
    sum = a+b
    count = 0
    while total_lambs >= b:
        total_lambs -=b
        count += 1
        a = b
        b = sum
        sum = a+b
    return count


print(solution(300))

#test cases for testing
def test_lamb_dist1():
    assert solution(10) == 1


def test_lamb_dist2():
    assert solution(143) == 3
