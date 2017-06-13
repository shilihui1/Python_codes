a = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
for key, value in enumerate(a):
    print(key, value)

b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for key, value in enumerate(b):
    print(key, value)

for key, value in enumerate(b, start = 5):
    print(key, value)
