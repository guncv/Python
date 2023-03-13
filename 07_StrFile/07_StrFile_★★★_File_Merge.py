def read_next(f):
    l =  []
    for i in f.readlines() :
        i = i.split()
        l.append([i[0][-2:],i[0],i[1]])
    return l

x = input().split()
f1 = open(x[0],"r")
f2 = open(x[1],"r")
l1 = read_next(f1)
l2 = read_next(f2)  
for i in range(len(l2)):
    l1.append(l2[i])
l_new = sorted(l1)
for i in range(len(l_new)) :
    print(l_new[i][1],l_new[i][2])