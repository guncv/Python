name = ["Robert","William","James","John","Margaret"\
    ,"Edward","Sarah","Andrew","Anthony","Deborah"]
nickname = ["Dick","Bill","Jim","Jack","Peggy","Ed"\
    ,"Sally","Andy","Tony","Debbie"]
dict = {}
for i in range(len(name)) :
    dict[name[i]] = nickname[i]
    dict[nickname[i]] = name[i]
m = int(input())
list_new = []
for i in range(m) :
    x = input()
    list_new.append(x)
for i in range(len(list_new)) :
    if list_new[i] not in dict : print("Not found")
    else : print(dict[list_new[i]])
