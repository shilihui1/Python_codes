class solution:
    def subarray_sums(x):
        n = len(x)
        sum_subarray = []
        # from length 1 to length n
        for i in range(1, n):
            # move the starting point for length i
            for j in range(n - i + 1):
                a = sum(x[j:j + i])
                sum_subarray.append(a)
        return sum_subarray
print(solution.subarray_sums([-1, 4, -3, 4, -5])) 
