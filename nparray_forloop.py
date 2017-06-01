'''for loop in numpy array, using nditer(c)'''
import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array(['a', 'b', 'c', 'd'])
c = np.array([a, b])
print(c)
print(type(c))

for i in c:
    print(i)

for i in np.nditer(c):
    print(i)
