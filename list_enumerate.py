a = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
for index, value in enumerate(a):
    print(index, value)

b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for index, value in enumerate(b):
    print(index, value)

for index, value in enumerate(b, start = 5):
    print(index, value)
