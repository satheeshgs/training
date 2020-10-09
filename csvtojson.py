import csv
import json

csvfile = open('uk-data-sept2020.csv', 'r')
jsonfile = open('uk-data-sept2020.json', 'w')

fieldnames = ("country","customerRequest","subject","caseId","description")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)
