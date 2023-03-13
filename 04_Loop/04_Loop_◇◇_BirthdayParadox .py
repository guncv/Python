P = float(input())
k = 1
t = 1
while True :
    t = (t*(365 -(k-1)))/365
    if 1-t < P :
        k +=1
    else : break
print(k)
