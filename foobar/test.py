def solution(s):
    k=1
    num =1
    s_div = split_string(s,k)
    while k<=int(len(s)/2):
        if(arr_compare(s_div)):
            num = len(s_div)
            break
        else:
            k+=1
            s_div = split_string(s,k)
    return num

def split_string(s, l):  # code to split a string based on indices
    indices = [i for i in range(0, len(s), l)]
    new_str = [s[index:index+l] for index in indices]
    return new_str

def arr_compare(arr):  # code to compare elements of an array
    first_element = arr[0]
    for i in range(1, len(arr)):
        if (arr[i] != first_element):
            return False
    return True



print(solution('abccababccab'))
