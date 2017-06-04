# list comprehension
res0 = [x*2 for x in [1,2,3]]
print(res0)
print(type(res0))
# generator
res00 = (x*2 for x in [1,2,3])
print(list(res00))
print(res00)
print(type(res00))

# lambda funtion
repeat_list = lambda x: x*2
print(repeat_list([1, 2, 3]))

double_list = lambda x: [num*2 for num in x]
print(double_list([1, 2, 3]))

# lambda funtion and map function
nums = [1,2,3,4]
res1 = map(lambda x: x*2, nums)
print(res1)
print(list(res1))

# lambda funtion and filter function
res2 = filter(lambda x: x > 0, nums)
print(res2)
print(list(res2))

# function
def lessThanFive(element):
    return element < 5
res3 = filter(lessThanFive, [1,2,5,8])
print(res3)
print(list(res3))
print(lessThanFive)
