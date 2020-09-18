def postprocess(prob):
    category = dict({0:'Order Booking',
                         1:'Offer Selection',
                         2:'Order or Delivery Status',
                         3:'Order Modification',
                         4:'Pricing and Availability',
                         5:'Delivery or Collection Issues*',
                         6:'Documentation',
                         7:'Quotation Request',
                         8:'Install/Set Up Support',
                         9:'Troubleshooting*',
                         10:'Digital Tool Support',
                         11:'Maintenance Support'})
    l = len(prob)
    maxprob = max(prob)

    for i in range(0,l):
        if(maxprob==prob[i]):
            index = i
            break

    if maxprob > 0.43:
        return {"Category":category.get(index)}
    else:
        return{"Category":"No Prediction"}
