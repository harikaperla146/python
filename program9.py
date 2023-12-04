#wapp to swap the values in the ascending order
#sort an array in one swap whose two elements is greater than the current element 
def sortArray(A):
    #base case 
    if len(A) <= 1:
        return 
    x = -1
    y = -1
    prev = A[0]
    #process each pair of adjacent elemenrs
    for i in range(1, len(A)):
        #if the previous element is f=greater than tha current element
        if prev > A[i]:
            #first occurrence of conflict
            if x == -1:
                x = i - 1
                y = i
            else:
                #second occurrance of conflict
                y = i
        prev = A[i]
    #swap the elements at index 'x' and 'y'
    swap(A, x, y)
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
a= [3,5,6,9,8,7]
sortArray(a)
print(a)