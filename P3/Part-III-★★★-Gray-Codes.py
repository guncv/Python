def gray_codes(n,k):
    first = ['0','1']
    for i in range(n-1):
        m = first[::-1]
        first += m
        for j in range(len(first)) :
            if j < len(first)/2 :
                first[j] = '0' + first[j]
            else :
                first[j] = '1' + first[j]
    return first

n = int(input())
k = int(input())

if n <= 0 and k <= 0 :
    print('Invalid n and k')

elif n <= 0 :
    print('Invalid n')

elif k <= 0 :
    print('Invalid k')

else :
    out = ''
    for i in range(1,k+1):
        if i <= k-1 :
            if len(str(i)) == 1:
                m = n
            elif len(str(i)) == 2 :
                m = n-1 
            else :
                m = n-3
        else :
            if len(str(i)) == 1:
                m = n-1
            elif len(str(i)) == 2:
                m = n-2
            else : m = n-3     
        out += str(i)+'-'*m
    print(out)
    
    l = gray_codes(n,k)
    rows = len(l)//k
    idx = 0
    for i in range(rows) :
        print(','.join(l[idx:idx+k]))
        idx += k

    if len(l)%k == 0 :
        pass

    else :
        print(','.join(l[idx:]))

