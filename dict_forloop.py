'''for loop in dictionary, using dictionary method a.items()'''
a = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# items method for dictionary
for key, value in a.items():
    print(str(key) + "--" + str(value))

# keys method for dictionary
for key in a.keys():
    print(key)

# values method for dictionary
for value in a.values():
    print(value)

print("\nBEGIN: REPORT\n")
# Iterate over the key-value pairs of kwargs
for keys, values in a.items():
    # Print out the keys and values, separated by a colon ':'
    print(str(keys) + ": " + values)
print("\nEND REPORT")
