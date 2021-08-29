from cs50 import get_int


def main():
    # get integer input from the user
    while True:
        user_choice = get_int("Height: ")
        if user_choice < 9 and user_choice > 0:
            break

    # call the print pyramid function to print the pyramid
    print_pyramid(user_choice)


def print_pyramid(number):
    '''
    prints a pyramid for mario to climb
    input: integer number between 1 to 8
    output: pyramid printed to console
    '''

    for i in range(number):
        for j in range(number - (i+1)):
            print(" ", end="")
        print("#" * (i+1))


if __name__ == "__main__":
    main()