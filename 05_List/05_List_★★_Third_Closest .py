import math
line = int(input())
l_x,l_y=[],[]
for i in range(line) :
    x,y = [float(e) for e in input().split()]
    l_x.append(x)
    l_y.append(y)
l =[]
for i in range(len(l_x)) :
    m = math.sqrt(l_x[i]**2 + l_y[i]**2)
    l.append(m)
n = l
n2 = sorted(n)
a = n2[2]
m = l.index(a)
print("#"+str(m+1)+":","("+str(l_x[m])+",",str(l_y[m])+")")

