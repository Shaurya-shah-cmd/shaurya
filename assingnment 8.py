#question 1
import numpy as np
random_array = np.random.rand(4, 2)
print("Random (4x2) array:\n", random_array)
empty_array = np.empty((4, 2))
print("\nEmpty (4x2) array:\n", empty_array)
full_array = np.full((4, 2), 7)
print("\nFull (4x2) array with 7:\n", full_array)
zeros_array = np.zeros((3, 5))
print("\nZeros (3x5) array:\n", zeros_array)
ones_array = np.ones((4, 3, 2))
print("\nOnes (4x3x2) array:\n", ones_array)


#question 2
matrix_2_to_10 = np.arange(2, 11).reshape(3, 3)
print("\n3x3 matrix with values 2 to 10:\n", matrix_2_to_10)


#question 3
null_vector = np.zeros(10)
null_vector[5] = 11
print("\nNull vector with sixth value as 11:\n", null_vector)


#question 4
array = np.arange(10)
reversed_array = array[::-1]
print("\nOriginal array:\n", array)
print("Reversed array:\n", reversed_array)

