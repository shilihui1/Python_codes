import numpy as np

a1 = np.random.rand(100)
a2 = np.random.rand(100)
a3 = np.random.rand(100)

# combine 3 lists into one multi-dimensional list
a = []
for i in range(100):
    a.append([a1[i], a2[i], a3[i]])
print(a)

print(type(a))
# find out the length of the list
print(len(a))
# find out the size of each element in the list
print(len(a[0]))
# find out the dimension of the list
print(np.shape(a))
