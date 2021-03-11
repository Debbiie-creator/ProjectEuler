# We need to start of by defining the gcd of 2 numbers as it is easier and straight-forward 
# after which we will find the lcm by multiplying the two numbers and dividing by the gcd
def Gcd(a, b):
    if a > b:
        num1 = a
        num2 = b
    else:
        num1 = b
        num2 = a
    r = num1 % num2
    while r != 0:
        num1, num2 = num2, r
        r = num1 % num2
    return num2

def Lcm(a, b):
    n = (a * b)/Gcd(a, b)
    return n
#Now that we can find lcm of two numbers, we can go ahead and find the lcm of multiple numbers by iteration
def LCM(l=[]):
    m = Lcm(l[0], l[1])
    for i in range(2, len(l)):
        m = Lcm(m, l[i])
    return int(m)
#Finally we can find the lcm of the 20 numbers
l = [a for a in range(1,20)]
print(LCM(l))
