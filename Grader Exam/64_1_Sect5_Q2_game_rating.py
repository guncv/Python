def rating(m,n) :
    s = str(25*(m + 1)*(n/10**7))
    m,n = s.split('.')
    return int(m)

d = {}
for i in range(int(input())) :
    x = input().split(' | ')

    if x[0] == 'Play' and len(x) == 4 :
        songLv = int(x[2])
        score = int(x[3])

        if x[1] not in d :
            d[x[1]] = [songLv,score,rating(songLv,score)]
        else :
            if rating(songLv,score) < d[x[1]][2] :
                pass
            elif rating(songLv,score) > d[x[1]][2] :
                d[x[1]] = [songLv,score,rating(songLv,score)]
            else :
                if songLv < d[x[1]][0] :
                    pass
                elif songLv > d[x[1]][0] :
                    d[x[1]] = [songLv,score,rating(songLv,score)]
                else :
                    if score < d[x[1]][1] :
                        pass
                    elif score > d[x[1]][1] :
                        d[x[1]] = [songLv,score,rating(songLv,score)]
                    else :
                        pass  

    elif len(x) == 1 and x[0] == 'Rating' :
        if len(d) <= 5 :
            n = 0 
            for i in d :
                n += d[i][2]
            print(n)
        else :
            l = []
            for i in d :
                l.append(d[i][2])
            l1 = sorted(l)[::-1][:5]
            
            n = 0
            for i in l1 :
                n += i
            print(n)

    elif len(x) == 2 and x[0] == 'Rating' :
        if x[1] not in d :
            print('0')
        else :
            print(d[x[1]][2])

    elif len(x) == 2 and x[0] == 'Detail' :
        if x[1] not in d :
            print(x[1] + ': ' + 'No play history')
        else :
            print(x[1] + ' | ' + str(d[x[1]][0]) + ' | ' + str(d[x[1]][1]) + ' | ' + str(d[x[1]][2]))
    
    else : 
        pass