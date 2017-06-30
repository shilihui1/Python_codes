class solution:
    def subarray_sum_largest(x):
        n = len(x)
        temp_largest = sum(x)
        # from length 1 to length n
        for i in range(1, n):
            # move the starting point for length i
            for j in range(n - i + 1):
                a = sum(x[j:j + i - 1])
                if a > temp_largest:
                    temp_largest = a
        return temp_largest
print(solution.subarray_sum_largest([-1, 4, -3, 4, -5]))
