def get_sum_second_largest(even_matrix,odd_matrix):
    if len(even_matrix)>=2:
        even_second_largest = even_matrix[-2]
    else:
        even_second_largest = float('-inf')
    if len(odd_matrix)>=2:
        odd_second_largest = odd_matrix[-2]
    else:
        odd_second_largest = float('-inf')
    return even_second_largest + odd_second_largest
size = int(input("enter the size of array: "))
matrix =[]
for i in range(size):
    element = int(input(f"enter element at {i} index: "))
    matrix.append(element)
even_matrix = matrix[::2]
odd_matrix = matrix[1::2]
even_matrix.sort()
odd_matrix.sort()
print(f"Sorted evn array:{even_matrix}")
print(f"Sorted odd array:{odd_matrix}")
sum_second_largest = get_sum_second_largest(even_matrix,odd_matrix)
print(f"Sum of second-largest numbers:{sum_second_largest}")