import string
def convex_polygon_area(p) :
    m = 0
    for i in range(len(p)) :
        if i == len(p)-1 :
            m+= p[-1][0]*p[0][1]
        else :
            m+= p[i][0]*p[i+1][1]
    for i in range(len(p)) :
        if i == len(p)-1 :
            m-= p[-1][1]*p[0][0]
        else : m-= p[i][1]*p[i+1][0]
    return abs(m)/2

def is_heterogram(s) :
    a = ""
    for i in s :
        if i in string.punctuation : pass
        elif i == " " : pass
        elif i.lower() in a : return False
        else : a += i.lower()
    return True

def replace_ignorecase(s,a,b) :
    m = len(a)
    n = ""
    i = 0
    while i < len(s) :
        if s[i:i+m].lower() == a.lower() : 
            n += b
            i += m
        else :
            n += s[i]
            i+=1
    return n


def top3(votes) :
    list_tops = []
    for i in votes :
        list_tops.append([-int(votes[i]),i])
    list_tops = sorted(list_tops)
    m = []
    for i in range(3) :
        m.append(list_tops[i][1])
    return m


    
    



for k in range(2):
 exec(input().strip())
