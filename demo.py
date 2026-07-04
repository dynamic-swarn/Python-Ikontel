import numpy as np


arr = np.arange(1, 21)
print(arr)
print("===========================================================================")
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print(matrix)
print("===========================================================================")


total = np.sum(matrix)
print("Sum:", total)
print("===========================================================================")


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even = arr[arr % 2 == 0]
print(even)

print("===========================================================================")

arr = np.array([-5, 2, -3, 8, -1, 4])
arr[arr < 0] = 0
print(arr)
print("===========================================================================")

arr = np.array([1, 2, 3, 4, 5])

reverse = arr[::-1]

print(reverse)
print("===========================================================================")


arr = np.array([1, 2, 2, 3, 4, 4, 5, 5, 6])
unique = np.unique(arr)
print(unique)
print("===========================================================================")



A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = np.dot(A, B)
print(result)
print("===========================================================================")




matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

transpose = matrix.T
print(transpose)
print("===========================================================================")




matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Row-wise Sum:")
for i in range(len(matrix)):
    print(sum(matrix[i]))


print("Column-wise Sum:")
for j in range(len(matrix[0])):
    total = 0
    for i in range(len(matrix)):
        total = total + matrix[i][j]
    print(total)




