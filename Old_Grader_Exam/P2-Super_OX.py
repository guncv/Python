import numpy as np

def error(l) :
    return np.any((l != 1) or (l!= 2))


m = int(input())
n = int(input())
l = np.ndarray((m,m),int)

for i in range(m) :
    l[i,:] = input().split()
print(error(l))



    