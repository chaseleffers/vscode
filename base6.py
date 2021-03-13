import math
divisors = []
base = 6
testnum = 5040
tensplace = math.log(testnum//(base-1), base)
emlist = []
prevnum = 0

def turtles(testnum, base, tensplace, prevnum):
    if tensplace > 0:
        for a in range(base):
            tempnum = prevnum + a*base**tensplace
            if tempnum > testnum: break
            if tempnum == testnum:
                emlist.append(tempnum)
                break
            templace = tensplace - 1
            turtles(testnum, base, templace, tempnum)
    else:
        for x in range(base):
            try:
                if testnum % (prevnum + x) == 0:
                    emlist.append(prevnum + x)
            except:
                pass
        prevnum = 0

turtles(5040, 6, 4, 0)
print(emlist)
print(len(emlist))

