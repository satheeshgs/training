from itertools import count

def solution(total_lambs):
    if total_lambs == 1:
        return 1    
    henchmen = stingy_lambs(total_lambs) - generous_lambs(total_lambs)
    return henchmen


def generous_lambs(total_lambs): #for the generous flow each lamb payout is multiplied by 2
    sum = 1
    for i in count(start=0, step=1):
        if total_lambs <= 0:
            return i
        sum *= 2
        total_lambs -= sum

def stingy_lambs(total_lambs): #for the stingy flow with a fibonacci series
    a = 0 
    b = 1
    sum = a+b
    for i in count(start = 0, step = 1):
        if total_lambs <= 0:
            return i
        a = b
        b = sum
        total_lambs -= b
        sum = a+b

for i in range(10,13):
    print(i, solution(i), generous_lambs(i), stingy_lambs(i))


def max_payouts(total_lambs):
    payout = 1
    for i in count(start=0, step=1):
        if total_lambs <= 0:
            return i
        payout *= 2
        total_lambs -= payout


def min_payouts(lambs):
    a, b = 0, 1
    for i in count():
        if lambs <= 0:
            return i
        a, b = b, a + b
        lambs -= b

#test cases for testing
def test_lamb_dist1():
    assert solution(10) == 1


def test_lamb_dist2():
    assert solution(143) == 3
