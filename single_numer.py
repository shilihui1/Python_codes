'''
Given an array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity.
'''
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
