a = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
index_remove = [1, 2]
b = [value for key, value in enumerate(a) if key not in index_remove]
print(b)
