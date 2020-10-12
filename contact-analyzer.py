import pandas as pd
import numpy as np
import json
import csv
import numpy as np
import Levenshtein as lev
import re

data = pd.read_csv("find-contact-oct9.csv")
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
data['fuzz1'] = ''
data['fuzz2'] = ''
data['ai-match'] = ''

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

#fuzzy logic search
for i in range(0, len(data)):
    data["fuzz1"].iloc[i] = lev.ratio(
        data["Contact Name"].iloc[i], data["Name1"].iloc[i])
    data["fuzz2"].iloc[i] = lev.ratio(
        data["Contact Name"].iloc[i], data["Name2"].iloc[i])
    if(data["fuzz1"].iloc[i] > 0.5 or data["fuzz2"].iloc[i] > 0.5):
        data["ai-match"].iloc[i] = "Correct"
    elif(data["fuzz1"].iloc[i] == 0 and data["fuzz2"].iloc[i] == 0):
        data["ai-match"].iloc[i] = "No Prediction"
    else:
        data["ai-match"].iloc[i] = "Partialy Correct/ Incorrect"

data.to_csv('process-report-oct9-v2.csv', index=False)
