'''Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers representing the array's elements.

Output Format

Print the sum of the array's elements as a single integer.

Sample Input

6
1 2 3 4 10 11
Sample Output

31
'''
f = open('/Users/lihuishi/Desktop/python codes/number_lines.txt')
row = 0
for line in f.readlines():
    if row == 0:
        n = line
    elif row == 1:
        arr = [int(arr_temp) for arr_temp in line.strip().split(' ')]
        print(arr)
        print('The sum of those {} numbers are {}'.format(n, sum(arr)))
    row += 1
