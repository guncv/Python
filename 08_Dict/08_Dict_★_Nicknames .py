x = int(input())
dict_new = {}
for i in range(x) :
    name,nickname = input().split(" ")
    dict_new[name] = nickname
    dict_new[nickname] = name
y = int(input())
list = []
for i in range(y) :
    names = input()
    if names in dict_new.keys() :
        list.append(dict_new[names])
    else : list.append("Not found")
for i in list :
    print(i)