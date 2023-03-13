d_name = {}
d_car = {}

for i in range(int(input())) :
    x = input().split()

    if ' '.join(x[:2]) in d_name :
        d_name[' '.join(x[:2])].append(' '.join(x[2:]))
    else :
        d_name[' '.join(x[:2])] = [' '.join(x[2:])]

    if x[3] in d_car :
        d_car[x[3]].append(' '.join(x[:2]))
    else :
        d_car[x[3]] = [' '.join(x[:2])]

print(d_name)
print(d_car)
for i in range(int(input())) :
    ope = input().strip()

    if ope in d_name :
        print(ope + ' --> ' + ', '.join(sorted(d_name[ope])))
    elif ope in d_car :
        print(ope + ' --> ' + ', '.join(sorted(d_car[ope])))
    else :
        print('Not found')