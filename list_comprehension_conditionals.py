a = [num**2 for num in range(10) if num % 2 == 0]
print(a)
b = [num**2 if num % 2 == 0 else 0 for num in range(10)]
print(b)
