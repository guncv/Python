d = {}
x = []

# Input Dict
for i in range(int(input())) :
    l = input().split()

    if l[0] == 'B' :
        if l[1] not in x :
            x.append(l[1])

        if l[2] in d :
            d[l[2]].append((l[1],l[3]))
        else :
            d[l[2]] = [(l[1],l[3])]
    
    if l[0] == 'W' :
        for i in d[l[2]] :
            if i[0] == l[1] :
                d[l[2]].remove(i)

# Who win
d_win = {}
for i in d :
    l1 = []
    for j in d[i] :
        l1.append(j[1])
    
    for m,n in d[i] :
        if n == sorted(l1)[-1] :
            if m in d_win :
                d_win[m].append(i)
                d_win[m][0] += int(n)
            else : 
                d_win[m] = [int(n),i]
            break

# Output
for i in sorted(x) :
    if i not in d_win :
        print(i+':  '+'$0')
    else :
        print(i +":  $"+str(d_win[i][0])+' -> '+' '.join(sorted(d_win[i][1:])))