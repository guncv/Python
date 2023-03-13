import string
x = input()
s = ""
for i in x :
    if i not in string.punctuation :
        s += i
    else : s +=" "
list = s.split(" ") 
list_new = []
for i in list :
    if i == "" : pass
    else : list_new.append(i)
new_x = ""
for i in range(len(list_new)) :
    if i == 0 : 
        list_new[i] = list_new[i].lower()
        new_x += list_new[i]
    else : 
        m = list_new[i][0].upper()
        new_x += m
        new_x += list_new[i][1:].lower()
print(new_x)
