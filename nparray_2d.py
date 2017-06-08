import numpy as np
a = np.array([[1, 5, 3, 8, 0], [4, 0, 7, 2, 1]])
print(type(a))
print(a.shape)
print(a[0])
print(a[0][1])
print(a[0, 1])
print(a[:, 1:3])
print(a[0, :])

# numpy array only contains single type data
print(np.array([[1, 5, '3', 8, 0], [4, 0, 7, 2, 1]]))
