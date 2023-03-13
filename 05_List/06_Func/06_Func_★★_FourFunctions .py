def make_int_list(x) :
    return [int(i) for i in x.split()]

def is_odd(e) :
    if e%2 == 0 :
        return False
    else : return True

def odd_list(alist) :
    new_list = []
    for i in range(len(alist)) :
        if alist[i]%2 != 0 :
            new_list.append(alist[i])
    return new_list
    
def sum_square(alist) :
    d = 0
    for i in range(len(alist)) :
        d += alist[i]**2
    return d

exec(input().strip())