import string
def rot(x) :
    old = string.ascii_lowercase+string.ascii_uppercase
    new = string.ascii_lowercase[13:]+string.ascii_lowercase[:13] \
    +string.ascii_uppercase[13:]+string.ascii_uppercase[:13]
    m = ""
    for i in range(len(x)) :
        if x[i] in string.punctuation : m += x[i]
        elif x[i] == " " or x[i] in string.digits : m+= x[i]
        else : 
            n = old.index(x[i])
            m += new[n]
    return m

x = input()
while x != "end" :
    print(rot(x))
    x = input()


                

    