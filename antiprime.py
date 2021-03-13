stack = {}
hyperdivisible = {}
Prime = []
maxdivis = 0

for x in range(5041):
    stack[x] = 0
    for y in range(x+1):
        try:
            if x%y == 0:
                stack[x] = stack[x] + 1
        except:
            pass
    if stack[x]> maxdivis:
        hyperdivisible[x] = stack[x]
        maxdivis = stack[x]
    if stack[x] == 2:
        Prime.append(x)

print(stack)
print('==========================')
print(hyperdivisible)
print('=======')
print(Prime)

