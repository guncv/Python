m = input().split(" ")
rank = ['F','D','D+','C','C+','B','B+','A']
ids,grades = [],[]
while m != ['q'] :
    ids.append(m[0])
    grades.append(m[1])
    m = input().split(" ")
uids = input().split(" ")
for i in range(len(uids)) :
    x = ids.index(uids[i])
    a = grades[x]
    b = rank.index(a)
    if a == "A" :
        grades[x] = a
    else :
        grades[x] = rank[b+1]
for i in range(len(ids)) :
    print(ids[i],grades[i])   


            







     
