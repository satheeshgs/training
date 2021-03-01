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
    for i in range(0, len(json)):
        if json["name"][i] == domain.lower():
            return json["filepath"][i], json["answers"][i]



#find the ancestor of a parent
def findParent(json, str):
    for i in range(0, len(json)):
        if json["parent"][i] == str.lower():
            return json["ancestor"][i]



#find the answer from the Q&A maker pairs in the json
def findAnswer(json, question):
    for i in range(0,len(json)):
        if json["question"][i] == question.lower():
            return json["answer"][i]

