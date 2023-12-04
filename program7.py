#wapp to rearrange of an array with alternate high and low elemnts
#utility function to swap elemnts 'A[i]' and 'a[j]' in the list 
def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
#funtion to rearrange the list such that every second element of the list is greater than its left and right elements
def rearrangeArray(A):
    #start from the second elemt and increment index by 2 for each iteration of the loop
    for i in range(1, len(A), 2):
        #if the previous element is greater than the current element 
        if A[i - 1] > A[i]:
            #swap the elements
            swap(A, i - 1, i)
A= [9,3,4,2,7,1,2,4]
rearrangeArray(A)
print(A)