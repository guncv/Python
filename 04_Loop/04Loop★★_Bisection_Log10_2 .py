L = 0
a = float(input())
U = a
s = 0
while U != 0 :
    U = U//10
    s += 1
U = s
x = (U+L)/2
while abs(a -10**x) > 10E-10*max(a,10**x) :
    if 10**x > a :  U = x
    elif 10**x < a : L = x
    x =(L+U)/2
print(round(x,6))
