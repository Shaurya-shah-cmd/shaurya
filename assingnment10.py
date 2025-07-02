 #question 1
import numpy as np
arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])
arr = np.nan_to_num(arr, nan=0)
print("After replacing NaN with 0:\n", arr)
arr[:, [2, 3]] = arr[:, [3, 2]]
print("After swapping columns 2 & 3:\n", arr)
arr_T = arr.T
print("Transpose:\n", arr_T)


#question 2
arr3d = np.random.rand(2, 3, 4)  # Shape (2, 3, 4)
print("Original shape:", arr3d.shape)
moved = np.moveaxis(arr3d, 0, 2)
print("New shape:", moved.shape)

#question 3
arr = np.array([[1, np.nan, 3],
                [4, 5, np.nan]])
col_mean = np.nanmean(arr, axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col_mean, inds[1])
print("NaN replaced with column mean:\n", arr)


#question 4
arr = np.array([[1, -2, 3], [-4, 5, -6]])
arr = np.where(arr < 0, 0, arr)
print("Negative values replaced with 0:\n", arr)


#question 5
import numpy as np
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
avg = (arr1 + arr2) / 2
print("Average of arrays:", avg)


#question 6
from scipy import stats
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
combined = np.vstack((arr1, arr2))
mean = np.mean(combined)
median = np.median(combined)
mode = stats.mode(combined, axis=None).mode[0]
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

#question 8
import numpy as np
A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])

B = np.array([9, -6, 17])
A_inv = np.linalg.inv(A)
X = A_inv @ B
print("Solution using inverse matrix:")
print(f"x = {X[0]:.2f}, y = {X[1]:.2f}, z = {X[2]:.2f}")
X2 = np.linalg.solve(A, B)
print("\nSolution using np.linalg.solve:")
print(f"x = {X2[0]:.2f}, y = {X2[1]:.2f}, z = {X2[2]:.2f}")


#question 9
import numpy as np
import matplotlib.pyplot as plt
subjects = ['Math', 'Physics', 'Chemistry', 'English', 'CS']
sem1_marks = [85, 78, 92, 74, 88]
sem2_marks = [90, 80, 95, 79, 91]
x = np.arange(len(subjects))
width = 0.35
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, sem1_marks, width, label='Semester 1', color='skyblue', edgecolor='black')
rects2 = ax.bar(x + width/2, sem2_marks, width, label='Semester 2', color='salmon', edgecolor='black')
ax.set_ylabel('Marks')
ax.set_title('Comparison of Semester 1 & Semester 2 Results')
ax.set_xticks(x)
ax.set_xticklabels(subjects)
ax.legend()
ax.set_ylim(0, 100)
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

