#This next problem is pretty straight-forward
s = 0
t = 0
for i in range(101):
    s += i
    t += (i**2)
print((s**2)-t)
