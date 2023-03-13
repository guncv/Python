def row_number(t,e) :
    for i in range(len(t)) :
        for j in range(len(t[0])) :
            if t[i][j] == e : return i
    
def flatten(t) :
    l = []
    for i in range(len(t)) :
        for j in range(len(t[0])) :
            if t[i][j] == 0 : pass
            else : l.append(t[i][j])
    return l

def inversions(x) :
    l = []
    m = 1
    for i in range(len(x)-1):
        n = m
        while n < len(x) :
            l.append([x[i],x[n]])
            n += 1
        m += 1
    n = 0
    for i in range(len(l)) :
        if l[i][0] > l[i][1] : n +=1
        else : pass
    return n

def solvable(t) :
    m = flatten(t)
    if len(t)%2 != 0 :
        if inversions(m)%2 == 0 : return True
        else : return False
    else :
        if inversions(m)%2 == 0 :
            if row_number(t,0)%2 == 0 : return False
            else : return True
        else : 
            if row_number(t,0)%2 == 0 : return True
            else : return False
 
exec(input().strip())