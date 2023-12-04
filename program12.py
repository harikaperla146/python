#wapp to sort given set of array and removes the duplicate and sort at the end of the same set
def sort_by_frequency(arr):
    #create a dictionaryy to store the frequency of each element 
    frequency_dict = {}
    for element in arr:
        #update the frequency count in the dictionary
        frequency_dict[element] = frequency_dict.get(element, 0)+ 1
    #sort the array based on frequency and then by the element it
    sorted_arr = sorted(arr,key = lambda x:(frequency_dict[x],x))
    return sorted_arr
#input tje number of test cases 
t = int(input())
for _ in range(t):
    #input the size of the array 
    n = int(input())
    elements = list(map(int,input().split()))
    #call the function to sort the array by frequency
    sorted_result = sort_by_frequency(elements)
    print(sorted_result)
