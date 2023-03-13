def pattern1(nrows,ncols):
    m,l1 = 1,[]
    for i in range(nrows) :
        l2 = []
        for j in range(ncols) :
            l2.append(m)
            m +=1
        l1.append(l2)
    return l1

def pattern2(nrows,ncols):
    l = [[0]*ncols for i in range(nrows)]
    m = 1
    for i in range(nrows) :
        n = m
        for j in range(ncols) :
            l[i][j] = n
            n += nrows
        m += 1
    return l    

def pattern3(N):
    l1,n,m = [],1,0
    for i in range(N):
        l2 = [0]*N
        for j in range(m,N):
            l2[j] = n
            n += 1
        l1.append(l2)
        m +=1
    return l1

def pattern4(N):
    l1,n,m = [],1,0
    for i in range(N):
        x = n
        l2 = [0]*N
        for j in range(m,N):
            l2[j] = x
            x += j+2
        l1.append(l2)
        m += 1
        n += m
    return l1

def pattern5(N):
    l1,n,m = [],1,0
    for i in range(N):
        a,x,l2 = n,N,[0]*N
        for j in range(m,N):
            l2[j] = a
            a += x
            x -= 1
        l1.append(l2) 
        m += 1
        n += 1
    return l1

def pattern6(N):
    l,num = [[0]*N for i in range(N)],1
    for idx in range(N) :
        if idx == 0 :
            for i in range(N):
                l[i][i] = num
                num += 1

        elif idx == N-1 :
            l[0][N-1] = num

        elif idx%2 != 0 :
            rows = N-idx-1
            cols = N-1
            for i in range(N-idx):
                l[rows][cols] = num
                num += 1
                rows -= 1
                cols -= 1

        elif idx%2 == 0 :
            rows = 0
            cols = idx 
            for i in range(N-idx):
                l[rows][cols] = num
                num += 1
                rows += 1
                cols += 1
    return l

exec(input().strip())