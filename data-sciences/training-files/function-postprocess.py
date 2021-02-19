def postprocess(i):
    thisdict =	{1: "Ford", 2: "Mustang", 3: 1964}
    try:
        for i in thisdict:
            print(thisdict[i])
    except:
        return("No Prediction")

y = postprocess(2)
print(y)
