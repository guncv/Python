f = open('C:/Users/User/OneDrive/เดสก์ท็อป/Python/07_StrFile/data.txt', "r")
l,x = [],input().split()
for i in f.readlines():
    i = i.split()
    if i[0][:2] == x[1][2:] : l.append(float(i[1]))
    else : pass
if len(l) == 0 : print("No data")
else : print(str(min(l)),str(max(l)),str(sum(l)/len(l)))
