#import necessary libraries
import pandas as pd
from helpers import *


def main():
    #ask for domain input from user and pass it to recursiveJson function
    
    user_input = input("Please choose your domain: 'hr' or 'finance' or 'it'\n")
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

        if leafNode(options):
            should_continue = True
        else:
            user_input = input(f"choose from the options \n{options}\n")
            user_question = user_input
    
    #send user question to Q&A maker after the leafnode is hit
    print(f"The question to be sent to Q&A maker is /{user_question}/")


#starting the main function
if __name__ == "__main__":
    main()
