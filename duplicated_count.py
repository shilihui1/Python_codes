# find out how many numbers are duplicated in a given array
input_vec = [1, 2, 1, 3, 3, 2, 0, 0, 0, 2]

def dup_count_1(a):
    n = len(a)
    dup_num = 0
    # duplicated elements set
    dup = []
    value = a[0]
    for i in range(n):
        if a[i] in dup and value not in a[i+1:]:
            dup_num += 1
            value = a[i]
        dup.append(a[i])
    
    return(dup_num)


print(dup_count_1(input_vec))    


def dup_count_2(a):
    n = len(a)
    a.sort()
    dup_num = 0
    value = a[0]
    if a[0] == a[1]:
        dup_num += 1
    for i in range(1, n - 1):
        if a[i] in a[i+1:] and value not in a[i+1:]:
            dup_num += 1
            value = a[i]
    return(dup_num)
print(dup_count_2(input_vec))
