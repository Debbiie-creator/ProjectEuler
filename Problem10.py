#Slow Algorithm
""" def lPrimes(n):
    s = 0
    x = 2
    while x < n:
        if cP(x):
            s += x
        x += 1
    return s
print(lPrimes(2000000)) """

#Faster Algorithm
#Note as we know that all primes apart from two are odd we can skip the even numbers and move ahead.
def LPrimes(n):
    s = 5
    x = 5
    while x < n:
        if cP(x):
            s += x
        x += 2
    return s
print(LPrimes(2000000))

