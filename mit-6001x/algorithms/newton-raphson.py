# Newton raphson method for polynomials https://en.wikipedia.org/wiki/Newton%27s_method
# when f(x) = 0 and the guess is g, then g-f(g)/f'(g) is a better approximation of the root

#finding square root of a number using newton raphson

epsilon = 0.01
num = float(input("Enter the number you want a square root for :"))

guess = num/2.0
numGuesses = 0

while abs(guess*guess - num) >= epsilon: #the polynomial is y^2 - num = 0
    numGuesses +=1
    guess = guess - ((guess*guess)-num)/(2*guess) #f(guess) = guess*guess -y; f'(guess) = 2*guess

print('numGuesses =:' + str(numGuesses))
print('Square root of '+str(num)+ ' is '+str(guess))