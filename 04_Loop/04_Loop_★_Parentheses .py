m = list(input())
l = [0]*len(m)
if m == "no parentheses" :
    print("no parentheses")
for i in range(len(m)) :
    if m[i] == "(" : l[i] = "["
    elif m[i] == "[" : l[i] = "("
    elif m[i] == ")" : l[i] = "]"
    elif m[i] == "]" : l[i] = ")"
    else : l[i] = m[i]
print("".join(l))


