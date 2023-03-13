import math
a,b,c,d = [int(e) for e in input().split()]
if a == 1 :
    c,d = d,c
    if b == 1 :
        c +=d
    elif b == 2 :
        c -= d
    elif b != 3 :
        c += c**d
    else : c = c/d
    a = (d + math.sqrt((c/b)**3+d))/(2+b*d)
else :
    if a == 2 :
        if b > 1 : c+=d
        else : pass
        if b > 2 : c = c/d
        else : pass
        if b > 3 : c += c**d
        else : a = math.log(c,10)
    else :
        while a > d :
            a -= 2
            if a < b :
                break
            else :
                c +=a

print(a,b,c,d)

     
