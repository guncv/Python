def factor(N) :
    dict_fac,k,l = {},2,[]
    while N > 1 :
        if N%k == 0 :
            dict_fac[k] = 1
            N = N/k
            while True :
                if N == 1 : break
                if N%k == 0 :
                    dict_fac[k] +=1
                    N = N/k
                else : break
        k += 1
    for i in dict_fac :
        l.append([i,dict_fac[i]])
    return sorted(l)

exec(input().strip())