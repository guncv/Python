line = int(input())
x,y = [0]*line,[0]*line
for i in range(line) :
    [x[i],y[i]] =[int(x) for x in input().split()]
z = input()
if z == "Zig-Zag" :
    print(min(x[0::2]+y[1::2]),max(x[1::2]+y[0::2]))
if z == "Zag-Zig" :
    print(min(x[1::2]+y[0::2]),max(x[0::2]+y[1::2]))

    
