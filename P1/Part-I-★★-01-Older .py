from typing import List


month = ["January","February","March","April","May",\
    "June","July","August","September","October",\
        "November","December"]
x1 = input().split(" ")
x2 = input().split(" ")
if int(x1[-1]) < int(x2[-1]) :
    print(x1[0])
elif int(x1[-1]) > int(x2[-1]) :
    print(x2[0])
else :
    if month.index(x1[1]) > month.index(x2[1]) :
        print(x2[0])
    elif month.index(x1[1]) < month.index(x2[1]) :
        print(x1[0])
    else :
        if int(x1[2].strip(",")) > int(x2[2].strip(",")) :
            print(x2[0])
        elif int(x1[2].strip(",")) < int(x2[2].strip(",")) :
            print(x1[0])
        else : 
            print(x1[0],x2[0])
