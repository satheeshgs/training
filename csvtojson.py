#import csv and json packages
import csv, json

csvpath = "batch-data.csv"
jsonpath = "batch-data.json"

data = {}
with open(csvpath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['Case ID']
        data[id]= rows

with open(jsonpath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))
