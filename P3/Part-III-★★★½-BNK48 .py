x = input()
operation = ['1','2','3']
dVote = {}
dOta = {}
dOshi = {}
l = []
l3 = []

# Input 
while x not in operation :
    voter,bnk,number = x.split()
    if bnk not in l3 :
        l3.append(bnk)

    if bnk in dVote :
        dVote[bnk] += int(number)
    else :
        dVote[bnk] = int(number)

    if bnk in dOta :
        if voter not in dOta[bnk] :
            dOta[bnk].append(voter)
    else :
        dOta[bnk] = [voter]

    if voter in dOshi :
        a = 0
        for i in dOshi[voter] :
            if bnk == i[1] :
                i[0] += -int(number)
                a += 1
        if a == 0 :
            dOshi[voter].append([-int(number),bnk])
    else :
        dOshi[voter] = [[-int(number),bnk]]
       
    x = input()

# Output
if x == '1' :
    l1 = []
    for i in dVote :
        l.append((dVote[i],i))

    n = 0
    for number,bnk in sorted(l)[::-1] :
        if n >= 3 : break
        else :
            l1.append(bnk)
            n += 1
    print(', '.join(l1))

elif x == '2' :
    l1 = []
    for i in dOta :
        l.append((len(dOta[i]),i))

    n = 0
    for ota,bnk in sorted(l)[::-1] :
        if n == 3 :break
        else :
            l1.append(bnk)
            n += 1
    print(', '.join(l1))

elif x == '3' :
    d_Oshi = {}
    for i in dOshi :
        m = sorted(dOshi[i])
        if m[0][1] in d_Oshi :
            d_Oshi[m[0][1]] += 1 
        else :
            d_Oshi[m[0][1]] = 1
    
    for i in d_Oshi :
        l.append([-d_Oshi[i],i])
    l1 = []
    n = 0

    for i in sorted(l) :
        if n == 3 : break
        l1.append(i[1])
        n +=1
    
    if len(l1) < 3 :
        for i in l3 :
            if i not in l1 :
                l1.append(i)
                
    print(', '.join(l1))