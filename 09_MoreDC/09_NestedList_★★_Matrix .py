def read_matrix() :
    m = []
    for k in range(int(input())) :
        x = input().split()
        r = []
        for e in x :
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c,a) :
    for i in range(len(a)) :
        for j in range(len(a[i])) :
            a[i][j] = c*a[i][j]
    return a

def mult(A,B) :
    l = []
    for i in range(len(A)) :
        l2 = []
        for j in range(len(B[0])) :
            m = 0
            for k in range(len(B)) :
                m += (A[i][k]*B[k][j])
            l2.append(m)
        l.append(l2)
    return l

exec(input().strip())