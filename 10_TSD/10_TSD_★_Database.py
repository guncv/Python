cou = input()
teach = input()
data = input()
courses = open(cou,'r')
database = open(data,'r')
l = []

for i in courses.readlines() :
    a,ownnumber = i.split(',')
    teachers = open(teach,'r')
    for j in teachers.readlines() :
        b,teacher = j.split(',')
        l.append((a,b,ownnumber[0:-1],teacher[0:-1]))
    teachers.close()

for i in database.readlines() :
    m,n = i.split(',')
    p = 0
    for a,b,ownnumber,teacher in l :
        if m == a and n[:-1] == b :
            print(ownnumber+','+teacher)
            p +=1
    if p == 0 : print('record error')