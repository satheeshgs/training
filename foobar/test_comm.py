s ='anilkumar'

index =[]
arr = list(s)

for i in range(0,len(s)):
    if s[i] == s[0]:
        index.append(i)   
index.append(len(s))

pattern = arr[0:index[1]]
i =1
length = len(s)
while length == len(s) and i<len(index)-1:
    if pattern == arr[index[i]:index[i+1]]:
        length = index[i]
    else:
        i+=1
        pattern=arr[0:index[i]]



print(pattern)
