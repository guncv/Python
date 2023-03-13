for i in range(int(input())) :
    m = input()
    c = 0
    for j in range(len(m)) :
        if m[j] == "." : c+=1
        else : break
    print("."*(c//2)+m[c:])
