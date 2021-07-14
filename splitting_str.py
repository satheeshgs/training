# splitting a string till they are in alphabetical order
def str_split(s, i):
    ret_str =s[i]
    while s[i]<=s[i+1]:
        ret_str = ret_str + s[i+1]
        i+=1
        if i == len(s)-1:
            break
    return ret_str, i

s = 'thupuifhkevfcri'
i = 0
first_str = ''
max_str = ''

# iterate through and figure out the longest string
while i < len(s)-1:
    first_str, i = str_split(s, i)
    if len(first_str) > len(max_str):
        max_str = first_str
#     elif len(first_str) == len(max_str):
#         if first_str[0] < max_str[0]:
#             max_str = first_str
    i+=1;

print('Longest substring in alphabetical order is: ' + max_str)
