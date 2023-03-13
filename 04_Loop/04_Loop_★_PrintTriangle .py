h = int(input())  
w = 2*h-1
m = int((w-1)/2)
print(" "*m+"*"+" "*m)
n =1
p = m-1
for i in range(h-2):
    print(" "*p+"*"+" "*n+"*"+" "*p)
    n +=2
    p -=1
print("*"*w)
    

