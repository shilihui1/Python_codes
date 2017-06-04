fh = open('/Users/lihuishi/Desktop/python codes/lines.txt')
print(type(fh))
for line in fh.readlines():
    print(line)
