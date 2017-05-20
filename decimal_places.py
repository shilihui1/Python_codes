
'''
Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeroes in the array compared to its size.

Sample Input
6
-4 3 -9 0 4 1         
Sample Output

0.500000
0.333333
0.166667
'''

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(str.format('{0:.6f}', sum(x>0 for x in arr)/n))
print(str.format('{0:.6f}', sum(x<0 for x in arr)/n))
print(str.format('{0:.6f}', sum(x==0 for x in arr)/n))
