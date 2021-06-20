def minimumMonthlyPaymentCalculator(balance, annualInterestRate):
    '''
    input: Total balance to be paid, annual interest rate charged
    returns: minimum monthly payment to pay off debt in a year
    '''
    def creditCardBalance(balance, monthlyInterestRate, minMonthlyPayment):
        '''
        input: Total balance to be paid, annual interest rate charged, minimum payment
        returns: boolean of balance less than or equal to zero
        '''
        months = 12
        #iterating to calculate balance at the end of the year
        while months != 0:
            unpaidBalance = balance - minMonthlyPayment
            balance = unpaidBalance*(1+monthlyInterestRate)
            months -= 1

        return balance

    monthlyInterestRate = annualInterestRate/12
    epsilon = 0.01 #defining epsilon
    #defining lower bound as the total balance divided by 12 and defining upper bound as total of (compounded interest+balance)/12
    lowerBound = balance/12
    higherBound = (balance*(1+monthlyInterestRate)**12)/12
    guess = (lowerBound+higherBound)/2
    remainingBalance = creditCardBalance(balance, monthlyInterestRate, guess)

    while abs(remainingBalance) > epsilon: #checking for the remaining balance to be within the epsilon specified
        #bisection search implementation
        if remainingBalance > 0:
            lowerBound = guess
        else:
            higherBound = guess
        guess = (lowerBound+higherBound)/2
        remainingBalance = creditCardBalance(balance, monthlyInterestRate, guess)
    return round(guess,2)


print('Lowest Payment: ' + str(minimumMonthlyPaymentCalculator(balance=999999, annualInterestRate=0.18))) #output should be 90325.03