import math

print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = math.floor((low+high)/2)

user_input = 'h'
while user_input:
    to_print = 'Is your secret number ' + str(guess) + '?'
    print(to_print)
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    while user_input not in ['h', 'l','c']:
        print("Sorry, I did not understand your input.")
        print(to_print)
        user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input == 'h':
        high = guess
    elif user_input == 'l':
        low = guess
    elif user_input =='c':
        print("Game over. Your secret number was: "+ str(guess))
        break
    
    guess = math.floor((low+high)/2)