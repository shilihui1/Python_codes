# only need to check whether x can be divided by a number from 1 to x/2
import math
def isprime(n):
    """ find out whether a given number n is a prime number or not"""
    if n == 1:
        print("1 is a special number")
        return False
    for x in range(2, math.ceil(n/2) + 1):
        if n % x == 0:
            print(n, "is not a prime number")
            return False
    else:
            print(n, "is a prime number")
            return True
        
for i in range(1, 24):
    print(isprime(i))
    
