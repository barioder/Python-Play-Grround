import numpy as np

# creating an array object

arr = np.array([[[1,2,3,4], [5,6,7,8], [4,2,3,4]], [[1,2,3,4], [5,6,7,8], [4,2,3,4]]])

print(arr)

# Printing the type of the array
print(f'Array is of type {type(arr)}')

#  Printing the array dimensions (axes)
print('NO of dimensions is ', arr.ndim)


# print shape of the array 
print('Shape of the array ', arr.shape )

# print size

print('Size of array', arr.size)

print('Adding a new axis')
a = np.array([1,2,3,4,5,6])
print(a)
a2 = a[np.newaxis, :]

print(a2)

a3 = a[:, np.newaxis]
print(a3)

a = np.array([[[1,2,3], [4,5,6]]])
print(a)
a3 = a[np.newaxis, :]

print(a3)

# create an array with n dimensions 

arr = np.array([1,2,3,5], ndmin=5)

print('arr has ',arr.ndim,'Dimensions')
print(arr)