l,l2,l_avg = [],[],[]
m,n = 0,0
for i in range(int(input())) :
    x = input().split()
    if x[0] == "next" :
        print("call",l[n])
        n +=1
    elif x[0] == "reset" : l.append(x[1])
    elif x[0] == "new" :
        print("ticket",l[m])
        l.append(str(int(l[m])+1))
        l2.append(x[1])
        m +=1
    elif x[0] == "order" :
        print("qtime",l[n-1],str(int(x[1])-int(l2[n-1])))
        l_avg.append(int(x[1])-int(l2[n-1]))
    elif x[0] == "avg_qtime":
        print("avg_qtime",str(sum(l_avg)/len(l_avg)))

        

    

