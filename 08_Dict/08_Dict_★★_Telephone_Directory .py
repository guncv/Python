x = int(input())
telephone = {}
for i in range(x) :
    m = input().split(" ")
    n = m[0]+" "+m[1]
    telephone[n] = m[2]
    telephone[m[2]] = n
y = int(input())
for i in range(y) :
    n = input()
    if n in telephone :
        print(n,"-->",telephone[n])
    else :print(n,"-->","Not found")