import math
def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def is_coprime(a,b,c):
    return gcd(gcd(a,b),gcd(b,c)) == 1

def primitive_Pythagorean_triples(max_len):
    triple,n = [],[]
    for i in range(1,max_len) :
        for j in range(2,max_len):
            c = math.sqrt(i**2 + j**2)
            if (c%1 == 0 and c <= max_len) and (is_coprime(i,j,c) and i <= j) :
                triple.append([int(c),i,j])
    m = sorted(triple)
    for i in range(len(m)):
        n.append([m[i][1],m[i][2],m[i][0]])
    return n

exec(input().strip())