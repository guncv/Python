x = int(input())
dict_icecream = {}
dict_number = {}
for i in range(x) :
    m = input().split(" ")
    dict_icecream[m[0]] = int(m[1])
    dict_number[m[0]] = 0
y = int(input())
for i in range(y) :
    m = input().split(" ")
    if m[0] in dict_icecream :
        dict_number[m[0]] += dict_icecream[m[0]]*int(m[1])
    else : pass
list_all = []
for i in dict_number :
    if dict_number[i] == 0 :
        pass
    else : list_all.append([dict_number[i],i])
if list_all == [] :
    print("No ice cream sales")
else :
    sum = 0
    for i in dict_number :
        sum += dict_number[i]
    print("Total ice cream sales:",round(float(sum),1))
    m = sorted(list_all)[::-1]
    list_icecream = []
    i = 1
    for i in range(len(list_all)) :
        if i == 0 :
            list_icecream.append(m[0][1])
        elif m[i][0] == m[0][0] :
            list_icecream.append(m[i][1])
            i += 1
        else : break
    n = sorted(list_icecream)
    print("Top sales:",", ".join(n))
