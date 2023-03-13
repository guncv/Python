list_del = []
while True :
    x = input()
    if x == "END" : break
    else : list_del.append(x.split(" "))
list_use = []
dict_month = {"1":31,"2":28,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31 \
    ,"9":30,"10":31,"11":30,"12":31}
dict_type = {"E":1,"Q":3,"N":7,"F":14}
for i in range(len(list_del)) :
    if int(list_del[i][4]) < 2558 : 
        print("Error:"," ".join(list_del[i]),"-->","Invalid year")
    elif list_del[i][3] not in dict_month : 
        print("Error:"," ".join(list_del[i]),"-->","Invalid month")
    elif list_del[i][3] == "2" :
        if (int(list_del[i][4])-543)%400 ==0 or \
           ((int(list_del[i][4])-543)%4 ==0 and \
               (int(list_del[i][4])-543)%100 !=0) :
            if int(list_del[i][2]) > 29 or int(list_del[i][2]) <= 0 :
                print("Error:"," ".join(list_del[i]),"-->","Invalid date")
            else :
                if list_del[i][1] not in dict_type :
                    print("Error:"," ".join(list_del[i]),"-->","Invalid delivery type")
                else : list_use.append(list_del[i])
        else :
            if int(list_del[i][2]) > 28 or int(list_del[i][2]) <= 0:
                print("Error:"," ".join(list_del[i]),"-->","Invalid date")
            else :
                if list_del[i][1] not in dict_type :
                    print("Error:"," ".join(list_del[i]),"-->","Invalid delivery type")
                else : list_use.append(list_del[i])
    elif int(list_del[i][2]) > dict_month[list_del[i][3]] or int(list_del[i][2]) <=0 :
        print("Error:"," ".join(list_del[i]),"-->","Invalid date") 
    elif list_del[i][1] not in dict_type :
        print("Error:"," ".join(list_del[i]),"-->","Invalid delivery type")
    else : list_use.append(list_del[i])
list_new = []
for i in range(len(list_use)) :
    list_new.append([list_use[i][0],list_use[i][1],int(list_use[i][2]),int(list_use[i][3]),int(list_use[i][4])])
for i in range(len(list_new)) :
    list_new[i][2] += dict_type[list_new[i][1]]
    if list_new[i][3] == 2 :
        if (list_new[i][4]-543)%400 ==0 or ((list_new[i][4]-543)%4 ==0 and (list_new[i][4]-543)%100 !=0) :
            if list_new[i][2] > 29  :
                list_new[i][3] += 1
                list_new[i][2] -=  29
            else : pass
        else :
            if list_new[i][2] > 28 :
                list_new[i][3] += 1
                list_new[i][2] -= 28
    elif list_new[i][3] == 12 :
        if list_new[i][2] > 31 :
            list_new[i][3] = 1
            list_new[i][4] +=1
            list_new[i][2] -= 31
        else : pass
    else :
        if list_new[i][2] > dict_month[str(list_new[i][3])] :
            list_new[i][2] -= dict_month[str(list_new[i][3])]
            list_new[i][3] += 1            
        else : pass
list_all = []
for i in range(len(list_new)) :
    list_all.append([list_new[i][4],list_new[i][3],list_new[i][2],list_new[i][0]])
list_x = sorted(list_all)
for i in range(len(list_x)) :
    print(list_x[i][3]+":","delivered on",str(list_x[i][2]) +"/"+str(list_x[i][1])+"/"+str(list_x[i][0]))
            