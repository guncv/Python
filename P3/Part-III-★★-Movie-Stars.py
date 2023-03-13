d = {}
for i in range(int(input())):   
    l1 = input().split(', ')
    for j in range(1,len(l1)):
        if l1[j] in d :
            d[l1[j]].append(l1[0])
        else :
            d[l1[j]] = [l1[0]]

l = [e.strip() for e in input().split(',')]

for i in l:
    if i not in d :
        print(i,'->','Not found')
    else :
        print(i,'->',', '.join(d[i]))
