import math
a = input()[1:-1].split(",")
b = input()[1:-1].split(",")
a = [float(a[0]),float(a[1]),float(a[2])]
b = [float(b[0]),float(b[1]),float(b[2])]
l = [float(a[0])+float(b[0]), float(a[1])+float(b[1]), float(a[2])+float(b[2])]
print(str(a),"+",str(b),"=",str(l))
