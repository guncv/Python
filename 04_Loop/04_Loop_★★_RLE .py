a = input()
l = [0]*len(a)
l.append(" ")
b = []
for i in range(len(a)) :
    l[i] = a[i]
n = 1
for i in range(len(a)) :
    if a[i] == l[i+1] :
        n += 1
    else :
        b.append(a[i])
        b.append(str(n))
        n=1
print(" ".join(b))


     

