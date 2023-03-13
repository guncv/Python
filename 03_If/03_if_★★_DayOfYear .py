d = int(input())
m = int(input())
y = int(input())
y -= 543
if m==1 :
    print(d)
if m==2 :
    print(31+d)
if m==3 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+d)
    else :
        print(31+28+d)
if m==4 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+31+d)
    else :
        print(31+28+31+d)
if m==5 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+31+30+d)
    else :
        print(31+28+31+30+d)
if m==6 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+31+30+31+d)
    else :
        print(31+28+31+30+31+d)
if m==7 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+31+30+31+30+d)
    else :
        print(31+28+31+30+31+30+d)
if m==8 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+31+30+31+30+31+d)
    else :
        print(31+28+31+30+31+30+31+d)
if m==9 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+31+30+31+30+31+31+d)
    else :
        print(31+28+31+30+31+30+31+31+d)
if m==10 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+31+30+31+30+31+31+30+d)
    else :
        print(31+28+31+30+31+30+31+31+30+d)
if m==11 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+31+30+31+30+31+31+30+31+d)
    else :
        print(31+28+31+30+31+30+31+31+30+31+d)
if m==12 :
    if (y %400 ==0) or (y%4 ==0 and y%100 !=0) :
        print(31+29+31+30+31+30+31+31+30+31+30+d)
    else :
        print(31+28+31+30+31+30+31+31+30+31+30+d)


        




