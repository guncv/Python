import string
f = open('data.txt','r')
for k in f.readlines() :
    l1 = []
    for i in k.split() :
        n = 0

        for j in i :
            if j in string.digits :
                n += 1
        
        if n == len(i) and i[0] != '0' :
            t = len(i)
            l = []

            while True :
                if t-3 >= 0 :
                    l.append(i[t-3:t])
                    t -= 3

                else :
                    if t == 0 : break
                    else :
                        l.append(i[:t]) 
                        break

            i = ','.join(l[::-1])
            l1.append(i)
        
        else :
            l1.append(i)
    print(' '.join(l1))

