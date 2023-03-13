def pattern1(N) :
    l = [[0 for i in range(N)] for j in range(N)]
    row = 0
    col_start = N-1
    m = 1
    for i in range(N) :
        col = col_start

        for j in range(N-col_start) :
            l[row][col] = m
            col += 1
            m += 1

        col_start -= 1
        row += 1
    return l

def pattern2(N) :
    l = [[0 for i in range(N)] for j in range(N)]
    col = 0
    m = 1
    t = 1
    for i in range(N) :
        row = 0

        for j in range(t) :
            l[row][col] = m
            m += 1
            row += 1
            
        col += 1
        t += 1
    return l

print(pattern2(5))