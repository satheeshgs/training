#import necessary libraries
import pandas as pd
import json

"""
#reading the necessary json and converting to a dataframe
json_data = pd.read_json("parsed-json.json")
"""

#function to recursively pass through the json and return the child value
def recursiveJson(json, parent):
    for i in range(0, len(json)):
        if json["parent"][i] == parent.lower():
            return (json["child"][i])

#function to check if returned child value is a leaf node or not
def leafNode(arr):
    if len(arr) > 0:
        return False
    else:
        return True

# function to return the domain specific json
def returnDomainJson(json, domain):
    for i in range(0,len(json)):
        if json["name"][i] == domain.lower():
            return json["filepath"][i]

def main():
    #ask for domain input from user and pass it to recursiveJson function
    
    user_input = input("Please choose your domain: 'hr' or 'finance'")
    """
    chosen_json = pd.read_json(returnDomainJson(domain))
    """
    #getting the json filepath for traversing based on domain
    json_data = pd.read_json("choose-domain.json")
    domain_json_path = returnDomainJson(json_data, user_input) 
    
    #setting json data to traverse based on domain
    json_to_traverse = pd.read_json(domain_json_path)

    #traversing the json and going to the leaf node based on user input
    should_continue = False
    while should_continue is False:
        options = recursiveJson(json_to_traverse, user_input)
        print(options)
        if leafNode(options):
            should_continue = True      
        else:
            user_input = input("choose from the options \n")
    
    print(user_question)


#starting the main function
if __name__ == "__main__":
    main()
