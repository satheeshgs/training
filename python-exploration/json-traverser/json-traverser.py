#import necessary libraries
import json
with open('C:\Users\SESA445854\Documents\Python-training\git-repos\training\parsed-json.json') as f:
  json_data = json.load(f)


#function to recursively pass through the json
def recursiveJson(json, string):
    for key in json:
        if json["parent"] == string:
            if json["child"] is not null:
                return json["child"]
            else:
                return "none"


#testing out with json example
recursiveJson(json_data, 'hr')
