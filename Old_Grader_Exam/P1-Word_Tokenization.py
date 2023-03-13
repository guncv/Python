l = []
l_len = []
l_repair = []
x = input()
n = 0

for i in range(int(input())) :
    word = input()
    l.append(word)

    if len(word) not in l_len:
        l_len.append(len(word))

l_len1 = sorted(l_len)[::-1]

for i in l_len1 :

    for j in l :
        if len(j) == i :
            if j in x and j not in l_repair:
                l_repair.append(j)
                in_dex = x.index(j)
                x = x[:in_dex] + " " + x[in_dex:in_dex+i] + " " + x[in_dex+i:]
print(x)

