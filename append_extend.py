a = [1, 2]
a.append(0)
print(a)
# a.append(3, 4) #append takes exactly one argument
b = [3, 4]
a.extend(b)
print(a)
a.append(b)
print(a)
