def isPrime(n):
    if i == 0 or i == 1:
        return 0
    for x in range(2, int(math.sqrt(n))):
        if (n % x == 0):
            return 0
    else:
            return 1
            

