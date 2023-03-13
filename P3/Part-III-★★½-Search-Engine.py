d = {}  # ใส่ไปใน Dict
for i in range(2*int(input())) :
    if i%2 == 0:
        x = input()
    else :
        d[x] = input().split()

# Search
m = input()
while m != '-1' :
    d2 = {}
    for i in d :
        n = 0
        repeat = []       
        for j in d[i] :
            if m == j :
                n +=1
            if j not in repeat:
                repeat.append(j)
        d2[i] = (n/len(d[i]))*(1/len(repeat))

    max = [['None',0]]
    for i in d2 :
        if d2[i] > max[-1][1] :
            max.append([i,d2[i]])

    if max[-1][1] == 0 :
        print('NOT FOUND')
    else :  
        print(max[-1][0])

    m = input()
