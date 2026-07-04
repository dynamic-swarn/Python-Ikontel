import matplotlib.pyplot as plt
import numpy as np

# 1. Plot two lines on the same graph
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()


# 2. Add labels and title to a graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Graph")
plt.show()

# 3. Change the line style and marker
x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.plot(x, y, linestyle="--", marker="o")
plt.show()

# 4. Display a grid on the graph
x = [1, 2, 3, 4, 5]
y = [2, 5, 8, 11, 14]

plt.plot(x, y)
plt.grid(True)
plt.show()

# 5. Create a horizontal bar chart
subjects = ["Python", "Java", "C++", "C"]
marks = [90, 80, 75, 85]

plt.barh(subjects, marks)
plt.xlabel("Marks")
plt.title("Student Marks")
plt.show()

# 6. Find the sum and average of all elements
arr = np.array([10, 20, 30, 40, 50])

print("Sum =", np.sum(arr))
print("Average =", np.mean(arr))


# 7. Transpose a matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Original Matrix:")
print(matrix)

print("Transpose Matrix:")
print(matrix.T)



# 8. Reshape a 1D array of 12 elements into a 3×4 matrix
arr = np.arange(1, 13)

matrix = arr.reshape(3, 4)

print(matrix)




# 9. Find all even numbers from an array
arr = np.array([10, 15, 22, 31, 40, 55, 60])

even = arr[arr % 2 == 0]

print("Even numbers:", even)


# 10. Multiply two NumPy arrays element-wise
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

result = arr1 * arr2

print("Result:", result)