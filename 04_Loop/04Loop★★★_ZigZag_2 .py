l_x = []
l_y = []
while True :
    m = input()
    if m == "Zig-Zag" or m == "Zag-Zig" :
        break
    else : 
        x,y = m.split(" ")
        l_x.append(x)
        l_y.append(y)
for i in range(len(l_x)) :
    l_x[i] = int(l_x[i])
    l_y[i] = int(l_y[i])
if m == "Zig-Zag" :
    print(min(min(l_x[0:len(l_x)+1:2]),min(l_y[1:len(l_y)+1:2])), \
        max(max(l_x[1:len(l_x)+1:2]),max(l_y[0:len(l_y)+1:2])))
if m == "Zag-Zig" :
    print((min(min(l_x[1:len(l_x)+1:2]),min(l_y[0:len(l_y)+1:2]))), \
        max(max(l_x[0:len(l_x)+1:2]),max(l_y[1:len(l_y)+1:2])))
 
        
  
    



