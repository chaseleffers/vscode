import math

x = 'hi'
l = [38.42, 44.67, 65.03, 78.15, 82.37, 99.01]
l2 = [44.66, 65.01, 82.29, 98.91, 116.37]
ans = []
count = 1

while True:
    x = input("What value would you like to use?: ")
    if x =="!":
        break
    else:
        l.append(float(x))

for y in l2:
    print(1.54/(2 * math.sin(y*0.0174533/2)))
    count += 1
    
