#
class Solution:
    def longestCommonPrefix(lists):
        newl = lists[0]
        if len(lists) > 1:
            for li in lists[1:]:
                newl = [x for x in newl if x in li]
            return newl
l1 = [[3,2,1], [3,2,1,4,5], [3,2,1,8,9], [3,2,1,5,7,8,9]]
print(Solution.longestCommonPrefix(l1))
l2 = ['hello', 'heaven', 'heavy']
print(Solution.longestCommonPrefix(l2))

#
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            #print(i)
            for string in strs[1:]:
                #print(string)
                #print(i >= len(string))
                #print(string[i] != strs[0][i])
                #print('string[i] is ' + string[i])
                #print('strs[0][i] is ' + strs[0][i])
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

print(Solution().longestCommonPrefix(["hello", "heaven", "heavy"]))


# 
def commonprefix(m):
    "Given a list of pathnames, returns the longest common leading component"
    if not m: return ''
    s1 = min(m)
    s2 = max(m)
    #print(s1)
    #print(s2)
    for i, c in enumerate(s1):
        #print(i)
        #print(c)
        #print(s2[i])
        if c != s2[i]:
            return s1[:i]
    return s1
print(commonprefix(["hello", "heaven", "heavy"]))

# for two strings
def CommonPrefix(s1, s2):
    out = ''
    for i, j in zip(s1, s2):
        if i != j:
            break
        out += i
    return out
print(CommonPrefix("hello", "heaven"))

