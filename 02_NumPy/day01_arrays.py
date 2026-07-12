import numpy as np
print('\n ===== NumPy Arrays =====')

# creating arrays

arr = np.array([10, 20, 30, 40, 50])

two_d_arr = np.array([
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9],
    [2, 4, 6, 8, 9]
])

arr_2 = np.arange(0,21,5) # 0 to 20 with step size of 5
arr_3 = np.zeros((3,3)) # 3x3 array of zeros
arr_4 = np.ones((4,4)) # 4x4 array of ones
arr_5 = np.arange(10,51,1) # Numbers from 10 to 50.
arr_6 = np.arange(20,61,2) # Even numbers from 20 to 60.
arr_7 = np.linspace(0,10,5) # printing 5 numbers from 0 to 10 with equal spacing
arr_8 = np.random.randint(1,100,10) # printing 10 random numbers from 1 to 100

# displaying arrays
print('1D Array: ', arr)
print('\nArange Array: ', arr_2.reshape(5,1))
print('\n3x3 Zero Matrix: ')
print(arr_3)
print('\n4x4 One Matrix: ')
print(arr_4)
print('\n10 Numbers from 10 to 50: ', arr_5)
print('\nEven Numbers from 20 to 60: ', arr_6)
print('\n5 Numbers from 0 to 10: ', arr_7)
print('\n10 Random Numbers from 1 to 100: ', arr_8)


# array properties
print('\nShape: ', arr_8.shape)
print('Size: ', arr_8.size)
print('Data Type: ', arr_8.dtype)
print('Number of Dimensions: ', arr_8.ndim)


# indexing and slicing
print('\nLast element of 1D Array: ', arr[-1])
print('Second Row of 2D Array: ', two_d_arr[1])
print('Third Column of 2D Array: ', two_d_arr[:,2])
print('Reversed Array: ', arr[::-1])


# modifying arrays
arr_8[:] = 100
print('\nReplacing all elements with 100: ', arr_8)

# reshaping arrays
reshape_arr = np.arange(12)
print('\n3x4 Matrix: ', reshape_arr.reshape(3,4))