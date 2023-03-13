import math
a = str(input())
b = (a[3]+a[10]+a[17]+a[24]+a[31])
c = (a[7]+a[12]+a[17]+a[22]+a[27])
B = int(b)
C = int(c)
x = B+C+10000
X = str(x)
if len(X) == 6:
    y = (X[2]+X[3]+X[4])
else:
    y = (X[1]+X[2]+X[3])
z = (int(y[1])+int(y[2])+int(y[0]))
Z = str(z)
if len(Z) == 2:
    Z = (Z[1])
elif len(Z) == 3:
    Z = (Z[2])
m = int(Z)
m += 1
if m == 1:
    print(y+"A")
elif m == 2:
    print(y+"B")
elif m == 3:
    print(y+"C")
elif m == 4:
    print(y+"D")
elif m == 5:
    print(y+"E")
elif m == 6:
    print(y+"F")
elif m == 7:
    print(y+"G")
elif m == 8:
    print(y+"H")
elif m == 9:
    print(y+"I")
elif m == 10:
    print(y+"J")
else:
    print("Error")
