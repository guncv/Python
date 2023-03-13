a = int(input())
b = len(str(a))
c = int(a)
if  b ==4 :
    c = c/1000
    c =round(c,1)
    print(str(c)+"K") 
elif 7 > b > 4 :
    c =c /1000
    c =round(c)
    print(str(c)+"K") 
elif b == 7 :    
    c =c/1000000    
    c =round(c,1)
    print(str(c)+"M")
elif 10 >b > 7 :
    c = c /1000000
    c =round(c)
    print(str(c)+"M")
elif b ==10 :
    c = c /1000000000
    c =round(c,1)
    print(str(c)+"B")
elif b >10 :
    c = c/1000000000
    c = round(c)
    print(str(c)+"B")
else :
    print(a)
     

