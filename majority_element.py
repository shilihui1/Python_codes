class solution:
    def majority_element(nums):
        l = len(nums)/2
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        for num in nums:
            if d[num] > l:
               return num

print(solution.majority_element([1, 4, 0, 4, 4]))
