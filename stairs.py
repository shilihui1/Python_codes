'''
Input Format

A single integer, , denoting the size of the staircase.

Output Format

Print a staircase of size  using # symbols and spaces.

Note: The last line must have  spaces in it.

Sample Input

6 
Sample Output

     #
    ##
   ###
  ####
 #####
######
'''

def  StairCase(n):
    for i in range(1, n+1):
        printer =' '*(n-i+1) + '#'*i
        print(printer, '\n')

StairCase(6)
