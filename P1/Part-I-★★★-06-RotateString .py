operator = input()
n = int(input())
list_string =[0]*n
for i in range(n) :
    string =input().strip()
    list_string[i] = string
m = False
for i in range(n) :
    if i == n-1 :
        break
    if len(list_string[i]) != len(list_string[i+1]):
        print("Invalid size")
        m = True
        break
    else : pass
if operator == "flip" and m == False :
    for i in range(n) :
        print(list_string[i][::-1])
if operator == "180" and m == False :
    for i in range(-1,-n-1,-1) :
        print(list_string[i][::-1])
if operator == "90" and m == False :
    b = 0
    k = n-1
    for i in range(len(list_string[0])) :
        p =[]
        for j in range(n) :            
            p.append(list_string[k][b])
            k -=1
        print("".join(p))
        b +=1
        k = n-1

        
        

