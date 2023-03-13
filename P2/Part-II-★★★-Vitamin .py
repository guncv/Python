n = int(input())
l_fruit = []
for i in range(n) :
    x = input().split()
    l_fruit.append(x)
operate = input().split(" ")
if operate[0] == "show" :
    for i in l_fruit :
        print(" ".join(i))
elif operate[0] == "get" :
    m = 0 
    for i in range(len(l_fruit)) :
        if l_fruit[i][0] == operate[1] : 
            print(" ".join(l_fruit[i]))
            m +=1
        else : pass
    if m == 0 : print(operate[1],"not found")
elif operate[0] == "avg" :
    m = []
    x = int(operate[1])
    for i in range(len(l_fruit)) :
        m.append(float(l_fruit[i][x]))
    print(round(sum(m)/len(m),4))
elif operate[0] == "max" :
    x = int(operate[1])
    m = []
    for i in range(len(l_fruit)) :
        m.append([-float(l_fruit[i][x]),l_fruit[i][0]])
    m2 = sorted(m)
    print(m2[0][1],str(-m2[0][0]))
elif operate[0] == "sort" :
    x = int(operate[1])
    m = []
    for i in range(len(l_fruit)) :
        m.append([float(l_fruit[i][x]),l_fruit[i][0]])
    m2 = sorted(m)
    n = []
    for i in range(len(m2)) :
        n.append(m2[i][1])
    print(" ".join(n))