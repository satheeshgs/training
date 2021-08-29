from cs50 import get_float


def main():
    # get a floating point input from the user for cash owed
    while True:
        cash_owed = get_float("Change owed: ")
        if cash_owed > 0:
            break

    # convert to coins
    coins = coin_converter(cash_owed)

    # printing out the coins
    print(str(coins))
    

def coin_converter(change):
    '''
    converts the change to number of coins
    input: change in floating value
    output: minimum number of coins required
    '''
    coins = 0
    change = change * 100

    # iterating an array of the coin types
    for i in [25, 10, 5, 1]:
        coins += change // i
        change = change % i

    return int(coins)


if __name__ == "__main__":
    main()