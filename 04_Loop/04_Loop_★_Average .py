p = []
while True :
    x = input()   
    if x != "q" :
        p.append(x)    
    else :
        break
for i in range(len(p)) :
    p[i] = float(p[i])
n = 0
for i in range(len(p)) :
    n += p[i]    
if n == 0 :
    print("No Data")
else :
    print(round(n/len(p),2))



        


     