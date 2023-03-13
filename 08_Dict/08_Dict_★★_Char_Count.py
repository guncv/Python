import string
x = input().lower()
count = {}
for i in x :
    if i not in string.ascii_lowercase : pass
    elif i in count :
        count[i] += 1
    else :
        count[i] = 1
list_old = []
for i in count :
    list_old.append([-int(count[i]),i])
list_new = sorted(list_old)
for i in range(len(list_new)) :
    print(list_new[i][1],"->",-list_new[i][0])


