x1 = input()
x2 = input()
y1 = x1.lower()
y2 = x2.lower()
y1_list = []
y2_list = []
for i in range(len(y1)) :
    if y1[i] == " " :
        pass
    else :
        y1_list.append(y1[i])
for i in range(len(y2)) :
    if y2[i] == " " :
        pass
    else :
        y2_list.append(y2[i])
for i in range(len(y2)) :
    if len(y1_list) != len(y2_list) :
        break
    elif y2[i] == " " :
        pass
    elif y2[i] in y1_list :
        y1_list[y1_list.index(y2[i])] = ""
    else :
        break
m = "".join(y1_list)
if m == "" :
    print("YES")
else : print("NO")