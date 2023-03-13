def spiral_square(n) :
    l = [[0 for i in range(n)] for j in range(n)]
    l[n//2][n//2] = 1
    x = 2
    m = 1
    row = n//2
    col = n//2 +1

    while x <= n*n  :
        
        for i in range(m) :
            if x == n*n :
                l[row][col] = x
                x += 1
                break
            if i == m-1 :
                l[row][col] = x
                x += 1
                row -= 1
            else :
                l[row][col] = x
                col += 1
                x += 1
        if x <= n*n :
            for i in range(m) :
                if i == m-1:
                    l[row][col] = x
                    col -= 1
                    x += 1
                else :
                    l[row][col] = x
                    row -= 1
                    x += 1

            m += 1
            for i in range(m) :
                if i == m-1 :
                    l[row][col] = x
                    row += 1
                    x += 1
                else :
                    l[row][col] = x
                    col -= 1
                    x += 1
            
            for i in range(m) :
                if i == m-1 :
                    l[row][col] = x
                    col += 1
                    x += 1
                else :
                    l[row][col] = x
                    row += 1
                    x += 1
            m += 1
        else : break
    return l

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))


exec(input().strip())