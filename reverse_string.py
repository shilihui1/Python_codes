class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        a = ''
        for i in range(n):
            a += s[n - i - 1]
        return a
print(Solution().reverseString('hello'))
