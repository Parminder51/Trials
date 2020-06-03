"""This a binary search function.
It uses recursion
The function takes two inputs:
A sorted Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
It will return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    l = len(input_array)
    if l==1 and input_array[0]!=value: #base code to stop recursion
        return -1
    #checking if length of the array is even or odd
    if l%2!=0:
        a = l//2+1
    else:
        a = l//2
    #proceeding as per length of the array
    if value==input_array[a]:
        return a          #also stops recursion
    elif value>input_array[a]:
        return binary_search(input_array[a+1:], value)
    else:
        return binary_search(input_array[:a], value)

#Some test cases
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))