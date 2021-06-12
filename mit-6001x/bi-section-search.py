#Bisection search is the algorithm for discarding half the search space for any incrementing problem
#Midpoint based search algorithm https://en.wikipedia.org/wiki/Bisection_method

def sqr_root(num):
    epsilon =  0.01
    high = num
    low = 0
    num_guesses = 0
    guess = (high+low)/2

    while abs(guess**2-num) >= epsilon:
        print('low = '+ str(low)+' high = '+ str(high))
        num_guesses += 1
        if guess**2 < num:
            low = guess
        else:
            high = guess
        guess = (low+high)/2
    
    return guess, num_guesses


ans, guess_num = sqr_root(23)
print("Square root is "+ str(ans) + ".")
print("Number of guesses taken = "+ str(guess_num))