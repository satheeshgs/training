def creditCardBalance(balance, annualinterestRate, monthlyPaymentRate):
    '''
    input: Total balance to be paid, annual interest rate charged, minimum monthly payment rate
    returns: None
    prints: remaining balance at the end of the year
    '''
    monthlyInterestRate = annualinterestRate/12
    months = 12 
    while months != 0:
        minMonthlyPayment = balance*monthlyPaymentRate
        unpaidBalance = balance - minMonthlyPayment
        balance = unpaidBalance*(1+monthlyInterestRate)
        months-=1
    
    return round(balance,2)

print(creditCardBalance(balance, annualInterestRate, monthlyPaymentRate))