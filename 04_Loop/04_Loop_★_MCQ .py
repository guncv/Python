a = input()
b = input()
if len(a) == len(b) :
    m = 0
    for i in range(len(b)) :
        if a[i] == b[i] :
            m +=1
    print(m)
else :
    print("Incomplete answer")
