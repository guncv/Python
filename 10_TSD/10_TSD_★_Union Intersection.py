x,l = int(input()),[]
if x == 0 : 
    print(0)
    print(0)
else:
    for i in range(x) :
        l.append(set(input().split()))
    m = set()
    for i in range(len(l)) :
        m = m |l[i]
    print(len(m))
    n = l[0]
    for i in range(1,len(l)):
        n = n & l[i]
    print(len(n))