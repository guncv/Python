l,l2 = [],[]
for i in range(int(input())) :
    l.append(input().split())
x = set(input().split())
for i in range(len(l)) :
    if x.issubset(set(l[i])) and l[i][0] not in x : l2.append(l[i])
if len(l2) == 0 : print("Not Found")
else :
    for i in sorted(l2) :
        print(" ".join(i))
