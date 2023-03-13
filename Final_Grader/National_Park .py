def read_np() :
    NP = dict()
    
    while True :
        d = input().split(' : ')

        if len(d) == 1 :
            break

        elif d[1] in NP :
            NP[d[1]] = NP[d[1]] | {d[0]}
        
        else :
            NP[d[1]] = {d[0]}
    return NP

def has_np(NP,p) :
    if p not in NP :
        return False
    return True

def find_parks(NP,p) :
    if p not in NP :
        return []
    else :
        x = list(NP[p])
        return sorted(x)

def print_greenest_province(NP) :
    l = []
    for i in NP :
        l.append(len(NP[i]))
    
    x = sorted(l)[-1]
    l1 = []
    for i in NP : 
        if len(NP[i]) == x :
            l1.append(i)
    
    print(','.join(sorted(l1)))


print(read_np())