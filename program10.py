#find the largest number possible from a given numbers
from functools import cmp_to_key
@cmp_to_key
def custom_compare(a,b):
    value1 = str(a) + str(b)
    value2 = str(b) + str(a)
    if value1 < value2:
        return 1
    elif value1 > value2:
        return -1
    else:
        return 0
def findLargestNumber(numbers):
    #sport using a custom function object
    numbers.sort(key=custom_compare)
    #join and return 
    return ''.join(map(str,numbers))
numbers = [10,68,97,9,21,12]
largestNumber = findLargestNumber(numbers)
print('the largest number is' , largestNumber)