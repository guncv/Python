pra = []
stroke = []
choose_or_not = []
for i in range(9) :
    x1,x2,x3 = [int(e) for e in input().split()]
    pra.append(x1)
    stroke.append(x2)
    choose_or_not.append(x3)
stoke_new = 0
for i in range(9) :
    if choose_or_not[i] == 1 :
        stoke_new += min(stroke[i],pra[i]+2)
    else : pass
stoke_together = 0
for i in range(9) :
    stoke_together += stroke[i]
pra_together = 0
for i in range(9) :
    pra_together += pra[i]
m = 1.5*(stoke_new) - pra_together
m2 = 0.8*m
m3 = str(m2)
index_m2 = m3.index(".")
print(stoke_together)
if m2 > 0 :
    print(m3[0:index_m2])
    score = stoke_together - int(m3[0:index_m2])
if m2 == 0 :
    print(0)
    score = stoke_together
if m2 < 0 :
    print(int(m3[:index_m2])-1)
    score = stoke_together - (int(m3[0:index_m2]) -1)
print(score)


