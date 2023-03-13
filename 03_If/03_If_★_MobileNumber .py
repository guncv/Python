a =str(input())
if a[0:2] in ["06","08","09"] :
    if len(a) == 10 :
        print("Mobile number")
    else :
        print("Not a mobile number")
else :
     print("Not a mobile number")