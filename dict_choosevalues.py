''' choose the even indexed values in a dictionary, i.e., ['b', 'd']'''
a = {1:'a', 2:'b', 3:'c', 4:'d'}
res = []
for key, value in a.items():
    if key % 2 == 0:
        res.append(value)
print(res)
