a,b,c,d = [float(x) for x in input().split()]
m = max(a,b,c,d)
n = min(a,b,c,d)
print(round((a+b+c+d-m-n)/2,2))

