class Solution:
    def maxvalue_count(a):
        a_enumerate = list(enumerate(a))
        print(a_enumerate)

        count = 0
        a_max = max(a)
        for key, value in enumerate(a):
            if value == a_max:
                count += 1 
        return count

print(Solution.maxvalue_count([3, 2, 1, 3]))
