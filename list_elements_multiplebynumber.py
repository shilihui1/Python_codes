'''populate a list with a for loop,
and one liner Python code using list comprehension'''
a = [1,2,3,4]
res = []
for num in a:
    res.append(num*2)
print(res)
# one liner using list comprehension
print([num*2 for num in a])
