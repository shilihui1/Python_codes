# find the 3rd largest element in an unsorted array: http://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
class Solution:
    def third_largest(a):
        n = len(a)
        top3_array = sorted(a[:3], reverse = True)
        for i in range(3,n):
            if top3_array[-1] < a[i]:
                top3_array.pop()
                top3_array.append(a[i])
                top3_array.sort(reverse = True)
        return(top3_array[-1])

        

print(Solution.third_largest([11, 2, 4, 4, 5, 6, 10, 8, -12]))

import random
import time

for i in range(1, 6):
    a = random.sample(range(10**(i+1)), 10**i)
    time_start = time.clock()
    print(Solution.third_largest(a))
    time_elapsed = (time.clock() - time_start)
    #print(str.format('{0:.6f}', time_elapsed))
    print("the 3rd largest element among", 10**(i+1), "numers are", Solution.third_largest(a), "with computation time", time_elapsed)
