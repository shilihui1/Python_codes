# two different conditional expression in Python: conditional execution and conditioal value
a, b = 1, 0
print("b ({}) is larger".format(b) if a < b else "a ({}) is larger".format(a))
