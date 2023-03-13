m,l,b = [],{},[]
for i in range(int(input())):
    x = input().split(",")
    m.append((x[0],x[1],x[2],x[3]))
for music,singer,typ,time in m :
    n = time.split(":")
    time = int(n[0])*60 + int(n[1])
    if typ not in l :
        l[typ] = time
    else : l[typ] += time
for i in l :
    b.append([l[i],i])
b2 = sorted(b)[::-1]
for i in range(len(b2)) :
    if b2[i][0]%60 < 10 : 
        b2[i][0] = str(b2[i][0]//60)+":"+"0"+str(b2[i][0]%60)
    else : b2[i][0] = str(b2[i][0]//60)+":"+str(b2[i][0]%60)
if len(b) <= 3 :
    for i in range(len(b2)):
        print(b2[i][1],"-->",b2[i][0])
else : 
    for i in range(3):
        print(b2[i][1],"-->",b2[i][0])
