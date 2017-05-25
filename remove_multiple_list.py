a = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
index_remove = [1, 2]
b = [v for i, v in enumerate(a) if i not in index_remove]
print(b)
