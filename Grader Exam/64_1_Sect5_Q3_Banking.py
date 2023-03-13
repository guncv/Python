def inf(x) :
    if x%1 != 0 :
        return x
    return int(x)

d = {}
for i in range(int(input())) :
    a,b,c = input().split()

    if (a,b) in d :
        d[a,b] += float(c)
    else : 
        d[a,b] = float(c)
    
x = input()
while x != 'exit' :
    a = x.split()

    if a[2] == 'withdraw' :
        if (a[0],a[1]) not in d :
            print('Transaction Failed')
        elif d[a[0],a[1]] < float(a[3]) :
            print('Transaction Failed')
        else :
            d[a[0],a[1]] -= float(a[3])
            print(a[0] + ' (' + a[1] + ') ' + str(inf(d[a[0],a[1]])))

    elif a[2] == 'deposit' :
        s = 0 
        for m,n in d:
            if n == a[1] and m != a[0] :
                s += 1
        if s != 0 :
            print('Transaction Failed')
        else :
            if (a[0],a[1]) not in d :
                d[a[0],a[1]] = float(a[3])
                print(a[0] + ' (' + a[1] + ') ' + str(inf(d[a[0],a[1]]))) 
            else :
                d[a[0],a[1]] += float(a[3])
                print(a[0] + ' (' + a[1] + ') ' + str(inf(d[a[0],a[1]])))

    elif a[2] == 'transfer' and len(a) == 5:
        if (a[0],a[1]) not in d :
            print('Transaction Failed')
        elif d[a[0],a[1]] < float(a[4]) :
            print('Transaction Failed')
        else :
            s = 0
            for m,n in d :
                if n == a[3] :
                    d[m,n] += float(a[4])
                    d[a[0],a[1]] -= float(a[4])
                    print(a[0] + ' (' + a[1] + ') ' + str(inf(d[a[0],a[1]])))
                    print(m + ' (' + n + ') ' + str(inf(d[m,n]))) 
                    s += 1
            if s == 0 :
                print('Transaction Failed')

    else :
        print('Transaction Failed')

    x = input() 
