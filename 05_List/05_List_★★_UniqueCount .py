x = [int(e) for e in input().split()]
l = []
xSort = sorted(x)
for i in range(len(xSort)) :
    if xSort[i] not in l :
        l.append(xSort[i])
print(len(l))
if len(l) > 10 :
    print(l[:10])
else :
    print(l)








