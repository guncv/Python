y = [float(x) for x in input().split()]
n = 0
for i in range(len(y)-1) :
    if y[i-1] < y[i] and y[i]> y[i+1] :
        n += 1 
print(n)