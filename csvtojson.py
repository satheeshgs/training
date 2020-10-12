import csv
import json

csvfile = open('json-data.csv', 'r')
jsonfile = open('json-data.json', 'w')

fieldnames = ("column","JSON Response")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)
