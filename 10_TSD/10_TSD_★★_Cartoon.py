x = input()
d = {}
l = []

while x != 'q' :
    a,b = x.split(',')
    if b in d :
        d[b].append(a)
    else :
        d[b] = [a]
        l.append(b)
    x = input()

for i in l :
    for j in d :
        if i == j :
            print(str(i).strip()+': '+', '.join(d[j]))