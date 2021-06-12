#import necessary libraries
import pandas as pd
from helpers import *


def main():
    #ask for domain input from user and pass it to recursiveJson function
    json_data = pd.read_json("choose-domain.json")
    domains_available = []

    #printing out the available domains list
    for i in range(0,len(json_data)):
        domains_available.append(json_data["name"][i])
    user_input = input(f"Please choose your domain: \n{domains_available}\n")

    #getting the json filepath for traversing based on domain
    domain_json_path, answer_json_path = returnDomainJson(json_data, user_input)
    
    #setting json data to traverse based on domain
    json_to_traverse = pd.read_json(domain_json_path)
    json_answers = pd.read_json(answer_json_path)
    
    #traversing the json and going to the leaf node based on user input
    should_continue = False
    while should_continue is False:
        options = recursiveJson(json_to_traverse, user_input)

        if leafNode(options):
            should_continue = True
        else:
            user_input = input(f"\nchoose from the options \n{options}\n")
            user_question = user_input
    
    #send user question to Q&A maker after the leafnode is hit
    print(f"\nThe question to be sent to Q&A maker is /{user_question}/\n \n")
    answer = findAnswer(json_answers, user_question) #this answer is currently from the json; needs to be fetched from Q&A maker
    print(f"The answer to the question is \n{answer}\n")
    


#starting the main function
if __name__ == "__main__":
    main()

