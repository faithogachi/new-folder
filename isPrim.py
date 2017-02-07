def isPrim():
    if x >= 2:
        for x in range(2, (int(math.sqrt(n)))):
            if (n % x == 0) or (x % 2 == 0):
                return 0
            else:
                return 1
for x in range(int(input("write a number to check the prime number: "))):
    if x == isPrim:
        print (x)

print ("prime No.:" + str(x))
