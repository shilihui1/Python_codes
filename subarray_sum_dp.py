''' 
define the largest subarray sum of a_0, ..., a_i is s(i),
then we have: s(i+1) = max(s(i), a_(i+1))
'''
class solution:
    def subarray_sum_largest(x):
        n = len(x)
        temp_largest = x[0]
        sum_largest = temp_largest
        for num in x[1:]:
            #temp_largest: moving the start index, the temporary subarray sum
            temp_largest = max(num, temp_largest + num)
            sum_largest = max(sum_largest, temp_largest)
        return sum_largest
print(solution.subarray_sum_largest([-1, 4, -3, 4, -5]))
