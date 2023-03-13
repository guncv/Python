import string
m = input()
a = list(string.digits)
for i in m :
    if i in a :
        n = a.index(i)
        a[n] = ""
    else : pass
list_new = []
for i in a :
    if i == "" : pass
    else : list_new.append(i)
if len(list_new) == 0 : print("None")
else : print(",".join(list_new))
 

