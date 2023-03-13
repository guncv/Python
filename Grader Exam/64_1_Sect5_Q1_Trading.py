n = int(input())
if n == 1:
    print('No results')
else:
    l = []
    for i in range(n):
        stuff = input().split(',')
        for j in stuff:
            l.append(float(j))
    print(l)
    #Fast EMA = 7 วัน , slow = 14 วัน
    def slow_ema(l):
        back = []
        total = 0
        day = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        for i in range(0,14):
            if i in day:
                total += (l[i])*(1/13)
        back.append(total)  
        for i in range(14,len(l)):
            back.append(((2/(1+13))*l[i]) + (back[i-13]*(1-(2/(1+13)))))
        return back
    
    def fast_ema(l):
        back = []
        total = 0
        day = [0,1,2,3,4,5,6]
        for i in range(0,7):
            if i in day:
                total += (l[i])*(1/6)
        back.append(total)  
        for i in range(7,len(l)):
            back.append(((2/(1+12))*l[i]) + (back[i-7]*(1-(2/(1+12)))))
        return back
    print(slow_ema(l))