p = input().split(" ")
run = input()
lengh = len(p)/2
int_lengh = int(lengh)
for i in range(len(run)) :
    if run[i] == "C" :
        p[:int_lengh],p[int_lengh:] = p[int_lengh:],p[:int_lengh]
    if run[i] == "S" :
        P = [0]*len(p)
        p1 = p[:int_lengh]
        p2 = p[int_lengh:]
        for j in range(int_lengh) :
            P[2*j] = p1[j]
            P[2*j+1] = p2[j]
            p = P
    else : pass
print(" ".join(p))
       



