def solution(s):
    # Your code here
    index =[]
    arr = list(s) #creating an array out of the string
    #finding the indices of the first element for pattern matching
    for i in range(0,len(s)):
        if s[i] == s[0]:
            index.append(i)   
    index.append(len(s))
    pattern = arr[0:index[1]] #intial pattern for comparison

    i =1
    length = len(s)
    while length == len(s) and i<len(index)-1:
        if pattern == arr[index[i]:index[i+1]]:
            length = index[i] #appending the length of the index which is repeating
            pattern = arr[0:index[i+1]]
        else:
            i+=1

    num = int(len(s)/length)
    return num



    

print(solution('satishsatishfather'))