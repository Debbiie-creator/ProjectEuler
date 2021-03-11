import math
n = int(input("Enter the number:"))
largest = 0

for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0:
        while n % i == 0:
            n = n / i
        if i >= largest:
            largest = i
print(largest)

    
