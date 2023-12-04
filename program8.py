#wapp to the zeros at the end of list 
def reorder(A):
    #'k' stores the index of the next avaliable position
    k = 0
    #do for each element 
    for i in A:
        #if the current element is non-zero, put the element at the next free position in the list 
        if i:
            A[k] = i
            k = k + 1
        #move all 0's to the end of the list (remaining indices) 
    for i in range(k, len(A)):
        A[i] = 0
A = [6,9,8,2,3,2,5,6,7,0,0,0,1]
reorder(A)
print(A)