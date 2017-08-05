'''
Given an array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity.
'''
# below is not linear runtime
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_exist = []
        for i in range(n):
            if nums[i] in num_exist:
                num_exist.remove(nums[i])
            else:
                num_exist.append(nums[i])
        return num_exist[0]
print(Solution().singleNumber([1, 2, 5, 4, 2, 1, 4]))

# bitwise exclusive or, O(N)
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if not A:
            return None
        p = A[0]
        for i in range(1, len(A)):
            print('p is ' + str(p))
            print('A[i] is ' + str(A[i]))
            p = p ^ A[i]
            print('p becomes ' + str(p))
        return p
print(Solution().singleNumber([1, 2, 5, 4, 2, 1, 4]))
