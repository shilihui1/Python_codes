def isprime(n):
    """ find out whether a given number n is a prime number or not"""
    if n == 1:
        print("1 is a special number")
        return False
    for x in range(2, n):
        if n%x == 0:
            print(n, "is not a prime number")
            return False
    else:
            print(n, "is a prime number")
            return True
        
for i in range(1, 24):
    print(isprime(i))
    
