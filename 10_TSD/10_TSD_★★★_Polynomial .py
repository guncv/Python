def add_poly(p1,p2) :
    d,l,l2={},[],[]
    for a,x in p1:
        for b,y in p2:
            if y==x :
                d[x]= a+b
                l.append([-x,a+b])
            else: pass
    for a,x in p1:
        if x in d :pass
        else : l.append([-x,a])
    for b,y in p2:
        if y in d : pass
        else : l.append([-y,b])
    n = sorted(l)
    for i in n:
        if i[1] == 0 : pass
        else : l2.append((i[1],-i[0]))
    return l2


def mult_poly(p1,p2):
    d,l,l2 = {},[],[]
    for a,x in p1 :
        for b,y in p2 :
            if x+y in d : d[x+y] += a*b
            else : d[x+y] = a*b
    for i in d:
        l.append((-i,d[i]))
    n = sorted(l)
    for i in n:
        l2.append((i[1],-i[0]))
    return l2
    



for i in range(3):
    exec(input().strip())