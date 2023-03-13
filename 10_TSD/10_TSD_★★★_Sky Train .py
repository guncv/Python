x = input()
l = []
l1 = []
l2 = []
l_rep = []
d = {}
while len(x.split()) == 2 :
    state1,state2 = x.split()
    l.append([state1,state2])
    x = input()
for i in l :
    if i[0] == x :
        l2.append(i[1])
        d[i[1]] = 1
    elif i[1] == x :
        l2.append(i[0])
        d[i[0]] = 1
    else : l1.append(i)
for j in l1 :
    if j[0] in d :
        l2.append(j[1])
    elif j[1] in d :
        l2.append(j[0])
    else : pass
l2.append(x)
for k in sorted(l2) :
    if k in l_rep :
        pass
    else :
        print(k)
        l_rep.append(k)

    


    

            
        