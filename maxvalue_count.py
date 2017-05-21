class Solution:
    def maxvalue_count(a):
        a_enumerate = list(enumerate(a))
        print(a_enumerate)

        count = 0
        for i, j in enumerate(a):
            if j == max(a):
                count += 1 
        return count

print(Solution.maxvalue_count([3, 2, 1, 3]))
