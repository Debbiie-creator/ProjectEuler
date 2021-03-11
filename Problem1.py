#First Algorithm
#s = 0
#for i in range(1000):
#    if i % 3 == 0 or i % 5 == 0:
#        s += i
#print(s)


#More efficient algorithm
target = 999
def sumdivisibleby(n):
    p = target // n
    return n * ((p) * (p + 1) / 2)

print(sumdivisibleby(3) + sumdivisibleby(5) - sumdivisibleby(15))
    
