d  = {}
l1 = []
for i in range(int(input())) :
    x = input().split(":")
    d[x[0]] = list(x[1].split(","))
    l1.append(x[0])
m,l = input(),[]
for i in d :
    for j in range(len(d[i])) :
        if (d[i][j] in d[m] and i not in l) and i != m : l.append(i) 
if len(l)== 0 : print("Not Found")     
else :
    for i in l1 :
        if i in l :
            print(i)

