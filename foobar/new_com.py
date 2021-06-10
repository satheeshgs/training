s = 'abccabcabccabc'
index =[]
arr = list(s)

for i in range(0,len(s)):
    if s[i] == s[0]:
        index.append(i)   
index.append(len(s))
pattern = arr[0:index[1]]

i =1
length = 0
while length == 0:
    if pattern == arr[index[i]:index[i+1]]:
        length = index[i]
    else:
        i+=1

num = int(len(s)/length)

print(arr)
print(index)
print(length)
print(pattern)
print(num)