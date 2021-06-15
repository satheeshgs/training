def minimumMonthlyPaymentCalculator(balance, annualInterestRate):
    '''
    input: Total balance to be paid, annual interest rate charged
    returns: minimum monthly payment to pay off debt in a year
    '''
    def creditCardBalance(balance, annualInterestRate, minMonthlyPayment):
        '''
        input: Total balance to be paid, annual interest rate charged, minimum payment
        returns: boolean of balance less than or equal to zero
        '''
        months = 12
        monthlyInterestRate = annualInterestRate/12
        #iterating to calculate balance at the end of the year
        while months != 0:
            unpaidBalance = balance - minMonthlyPayment
            balance = unpaidBalance*(1+monthlyInterestRate)
            months -= 1

        return balance

    minMonthlyPayment = 10
    while creditCardBalance(balance, annualInterestRate, minMonthlyPayment) > 0:
        minMonthlyPayment += 10
    
    print('Lowest Payment: '+ str(minMonthlyPayment))


minimumMonthlyPaymentCalculator(balance=320000, annualInterestRate = 0.2)
