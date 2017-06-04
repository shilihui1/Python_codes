# list comprehension
a = [num for num in range(10)]
print(a)
print(type(a))

# generator
b = (num for num in range(10))
print(b)
print(type(b))
print(list(b))
