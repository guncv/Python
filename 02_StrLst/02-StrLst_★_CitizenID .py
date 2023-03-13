m = input()
n =(11 -((13*int(m[0])+12*int(m[1])+11*int(m[2])+10*int(m[3])+9*int(m[4]) \
+8*int(m[5])+7*int(m[6])+6*int(m[7])+5*int(m[8])+4*int(m[9])+3*int(m[10]) \
    +2*int(m[11]))%11))%10
print(m[0],m[1:5],m[5:10],m[10:12],str(n))