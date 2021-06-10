import pandas as pd
import numpy as np
import json
import csv
import numpy as np
import Levenshtein as lev
from fuzzywuzzy import fuzz

data = pd.read_csv("find-contact-oct16v1.csv")
#converting the data to be compared into lower case
data["Contact Name"] = data["Contact Name"].str.lower()
data["Predicted Contact"] = data["Predicted Contact"].str.lower()

#finding names: Remove " and / from the JSON Response before proceeding
data["JSON Response"] = data["JSON Response"].str.replace('"','')
names = []
for i in range(0, len(data)):
    d = data["JSON Response"].iloc[i]
    start = d.find('contactName: [') + len('contactName: [')
    end = d.find(']')
    nm = (d[start:end])
    names.append(nm)

data["Name"] = names
data['Name1'] = ''
data['Name2'] = ''
#data['lev1'] = ''
#data['lev2'] = ''
data['fuzz1'] = ''
data['fuzz2'] = ''
#data['ai-match'] = ''
data['ai-match1'] = ''

#separating the names to separate columns
for i in range(len(data)):
    arr = data['Name'].iloc[i].split(', ')
    try:
        data['Name1'].iloc[i] = arr[0]
    except IndexError:
        pass
    try:
        data['Name2'].iloc[i] = arr[1]
    except IndexError:
        pass

#levenshtein ratio
#for i in range(0, len(data)):
#    data["lev1"].iloc[i] = lev.ratio(data["Contact Name"].iloc[i], data["Name1"].iloc[i])
#    data["lev2"].iloc[i] = lev.ratio(data["Contact Name"].iloc[i], data["Name2"].iloc[i])
#    if(data["lev1"].iloc[i] > 0.5 or data["lev2"].iloc[i] > 0.5):
#        data["ai-match"].iloc[i] = "Correct"
#    elif(data["lev1"].iloc[i] == 0 and data["lev2"].iloc[i] == 0):
#        data["ai-match"].iloc[i] = "No Prediction"
#    else:
#        data["ai-match"].iloc[i] = "Partialy Correct/ Incorrect"

#fuzzy logic search
for i in range(0, len(data)):
    data["fuzz1"].iloc[i] = fuzz.token_set_ratio(data["Contact Name"].iloc[i], data["Name1"].iloc[i])
    data["fuzz2"].iloc[i] = fuzz.token_set_ratio(data["Contact Name"].iloc[i], data["Name2"].iloc[i])
    if(data["fuzz1"].iloc[i] > 75 or data["fuzz2"].iloc[i] > 75):
        data["ai-match1"].iloc[i] = "Correct"
    elif(data["fuzz1"].iloc[i] == 0 and data["fuzz2"].iloc[i] == 0):
        data["ai-match1"].iloc[i] = "No Prediction"
    else:
        data["ai-match1"].iloc[i] = "Partialy Correct/ Incorrect"

data.to_csv('process-report-oct16v1.csv', index=False)
