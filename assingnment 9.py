import numpy as np
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
combined = np.vstack((a, b))
print(combined)
a = np.array([10, 11])
b = np.array([[4, 5, 6],
              [7, 8, 9]])
a_col = a[:, np.newaxis]
combined = np.hstack((b, a_col))
print(combined)

#question 2
import numpy as np
b = np.array([[1, 2, 3],
              [4, 5, 6]])
flat = b.flatten()
print(flat)
flat2 = b.ravel()
print(flat2)
flat3 = b.reshape(-1)
print(flat3)
#question 3
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)
b = np.array([[1, 2, 3],
              [4, 5, 6]])
reverse_rows = b[::-1]
print(reverse_rows)
reverse_cols = b[:, ::-1]
print(reverse_cols)

#question 4
import numpy as np
arr = np.array([10, 20, 5, 7, 35])
max_val = np.max(arr)
print("Max:", max_val)
min_val = np.min(arr)
print("Min:", min_val)
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
rows, cols = arr2d.shape
print("Rows:", rows)
print("Columns:", cols)
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
elem = arr2d[1, 2]
print("Element at (2nd row, 3rd col):", elem)
print("All elements:")
for row in arr2d:
    for item in row:
        print(item, end=' ')
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
total = 0
for row in arr2d:
    for item in row:
        total += item
print("Sum using for loop:", total)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
add = a + b
print("Addition:", add)
sub = a - b
print("Subtraction:", sub)
mul = a * b
print("Multiplication:", mul)
div = a / b
print("Division:", div)


