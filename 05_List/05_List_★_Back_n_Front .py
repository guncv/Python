line = int(input())
l =[0]*line
if line != 0 : 
    for i in range(line) :
        m1 = int(input())
        l[i] = m1
x = [int(e) for e in input().split()]
for i in range(len(x)) :
    l.append(x[i])
while True :
    m2 = int(input())
    if m2 == -1 :
        break
    else :
        l.append(m2)
l_output = []
n =0
for i in range(len(l)) :
    if i%2 == 0 :
        l_output.append(l[i])
    if i%2 != 0 :
        l_output.insert(0,l[i])
print(l_output)

