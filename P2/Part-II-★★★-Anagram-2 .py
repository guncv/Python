import string
x1 = input()
x2 = input()
dict_1 = {}
dict_2 = {}
m = x1.lower()
n = x2.lower()
for i in range(len(m)) :
    if m[i] in string.punctuation or m[i] == " " : 
        pass
    elif m[i] in dict_1 : dict_1[m[i]] += 1
    else : dict_1[m[i]] = 1
for i in range(len(n)) :
    if n[i] in string.punctuation or n[i] == " " :
        pass    
    elif n[i] in dict_2 : dict_2[n[i]] += 1
    else : dict_2[n[i]] = 1
dict1_remove = {}
dict2_remove = {}
for i in dict_1 :
    if i not in dict_2 :
        dict1_remove[i] = dict_1[i]
    else : 
        if dict_1[i] > dict_2[i] :
            dict1_remove[i] = dict_1[i]-dict_2[i]
        else : pass
for i in dict_2 :
    if i not in dict_1 :
        dict2_remove[i] = dict_2[i]
    else :
        if dict_2[i] > dict_1[i] :
            dict2_remove[i] = dict_2[i]-dict_1[i]
        else : pass
list1 = []
list2 = []
for i in dict1_remove :
    list1.append([i,dict1_remove[i]])
for i in dict2_remove :
    list2.append([i,dict2_remove[i]])
list1 = sorted(list1)
list2 = sorted(list2)
print(x1)
if len(list1) == 0 : print(" - None")
else : 
    for i in range(len(list1)) :
        if list1[i][1] > 1 :
            print(" - remove",str(list1[i][1]),list1[i][0]+"'s")
        else : print(" - remove",str(list1[i][1]),list1[i][0])
print(x2)
if len(list2) == 0 : print(" - None")
else : 
    for i in range(len(list2)):
        if list2[i][1] > 1 :
            print(" - remove",str(list2[i][1]),list2[i][0]+"'s")
        else : print(" - remove",str(list2[i][1]),list2[i][0])

