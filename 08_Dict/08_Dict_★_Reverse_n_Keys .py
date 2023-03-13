def reverse(d) :
    dict_new = {}
    for i in d :
        m = d[i]
        dict_new[m] = i
    return dict_new


def keys(d,v) :
    list = []
    for i in d :
        if d[i] == v :
            list.append(i)
        else : pass
    return list

exec(input().strip())