def knows(R,x,y) :
    if y in R[x] :  return True
    else : return False

def is_celeb(R,x) :
    if x in R and (R[x] == set() or R[x] == {x}) :
        for i in R :
            if i == x : pass
            elif x in R[i] : pass
            else : return False
        return True
    return False

def find_celeb(R) :
    l = []
    for i in R :
        if is_celeb(R,i) :
            l.append(i)
    if len(l) == 0 :
        return None
    else : return (' '.join(l)).strip()

def read_relations() :
    R = dict()
    x = input()
    m = set()
    while x != 'q' :
        a,b = x.split()
        if a in R : R[a] = set(b) | R[a]
        else : R[a] = set(b)
        m = m | (set(b) | set(a))
        x = input()
    n = list(m)
    for i in n :
        if i not in R :
            R[i] = set()
    return R

def main() :
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else : 
        print(c)

exec(input().strip())