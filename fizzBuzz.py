class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = '[\n'
        for i in range(1, n):
            if i%15 == 0:
                a += '"FizzBuzz"' + ',\n'
            elif i%3 == 0:
                a += '"Fizz"' + ',\n'
            elif i%5 == 0:
                a += '"Buzz"' + ',\n'
            else:
                a  += '"' + str(i) + '"' + ',\n'
        if n%15 == 0:
            a  += '"FizzBuzz"'
        elif n%3 == 0:
            a += '"Fizz"'
        elif n%5 == 0:
            a += '"Buzz"'
        else:
            a += '"' + str(n) + '"'
        a += '\n]'
        return a
print(Solution().fizzBuzz(15))
