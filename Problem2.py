#Defining function for finding the nth term in the Fibonacci sequence
def fib(n):
    k = 0
    i = 0
    j = 1
    s = 0
    while k < n:
        s = i + j
        i = j
        j = s
        k += 1
    return s

n = 0
s = 0
while fib(n) <= 4000000:
    if fib(n) % 2 == 0:
        s += fib(n)
    else:
        pass
    n += 1
print(s)

# Faster algorithm 
def sum_even_fib(n):
    i = 0
    j = 1
    s = 0
    fibSum = 0
    while s < n:
        s = i + j
        i = j
        j = s
        if s % 2 == 0:
            fibSum += s
        else:
            pass
    return fibSum
print(sum_even_fib(4000000))
    
