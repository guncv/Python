def first_fit(L,e) :
    m = 0
    for i in range(len(L)) :
        if sum(L[i]) + e <= 100 : 
            L[i].append(e)
            break
        else : m+=1
    if m == len(L) : L.append([e]) 
    return L

def best_fit(L,e) :
    l = []
    for i in range(len(L)) :
        l.append(100-(sum(L[i])+e))
    l_sort = sorted(l)
    m = 0
    for i in range(len(l_sort)) :
        if l_sort[i] >= 0 :
            L[l.index(l_sort[i])].append(e)
            break
        else : m+=1
    if m == len(l_sort) : L.append([e])
    return L

def partition_FF(D):
    l = []
    l.append([D[0]])
    for i in range(1,len(D)) :
        l = first_fit(l,D[i])
    return l

def partition_BF(D):
    l = []
    l.append([D[0]])
    for i in range(1,len(D)):
        l = best_fit(l,D[i])
    return l

exec(input().strip())