n = int(input())
l =[]
l.append(str(n))
while n!= 1 :     
    if n%2 == 0 :
        n = n//2
        l.append(str(n))
    else :
        n = 3*n +1
        l.append(str(n))
if len(l) > 15 :
    l2 = l[-15:]
    for i in range(len(l2)) :
        if i<len(l2)-1 :
            print(l2[i]+"->",end="")
        else :
            print(l2[i])
else :
    for i in range(len(l)) :
        if i <len(l)-1 :
            print(l[i]+"->",end="")
        else :
            print(l[i])


   