#Brute Force
#Defining a function to check if a number is prime
def checkPrime(x):
    for i in range(2, int(x**(0.5))+ 1):
        if x % i == 0:
            return False
    else:
        return True
#Defining a function to give the nth prime
def givePrime(n):
    i = 0
    x = 2 
    while i < n:
        if checkPrime(x)==True:
            i += 1
        if i < n:
            x += 1
    return x

print(givePrime(10001)) 

#There could be a better algorithm for this problem
