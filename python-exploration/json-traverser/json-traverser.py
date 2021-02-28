#import necessary libraries
import json
import pandas as pd

json_data = pd.read_json("parsed-json.json")

"""
with open('parsed-json.json') as f:
  json_data = json.load(f)
"""

print(type(json_data))
print(json_data)

"""
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
"""