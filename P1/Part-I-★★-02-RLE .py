m = input()
if m == "str2RLE" :
    n =input()
    l = [0]*len(n)
    l.append("")
    b = []
    x = 1
    for i in range(len(n)):
        l[i] = n[i]
    for i in range(len(n)) :
        if n[i] == l[i+1] :
            x +=1
        else :
            b.append(n[i])
            b.append(str(x))
            x =1
    print(" ".join(b))
elif m == "RLE2str" :
    n = input().split(" ")
    for i in range(len(n)//2) :
        print(n[2*i]*int(n[2*i+1]),end='')
else :
    print("Error")



