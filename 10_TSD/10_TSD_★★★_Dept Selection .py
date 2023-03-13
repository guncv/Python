d,l,l2 = {},[],[]
for i in range(int(input())):
    x = input().split()
    d[x[0]] = int(x[1])
for i in range(int(input())):
    x = input().split()
    l.append([-float(x[1]),x[0],x[2],x[3],x[4],x[5]])
for i in sorted(l) :
    for j in range(2,len(i)):
        if d[i[j]] > 0 : 
            l2.append([i[1],i[j]])
            d[i[j]] -= 1
            break
        else : pass 
for i in sorted(l2):
    print(" ".join(i))
