def is_odd(n) :
    if n%2 != 0 :
        return True
    else : return False

def has_odds(x) :
    for i in range(len(x)) :
        if x[i]%2 != 0 :
            return True
        else : pass
    return False

def all_odds(x) :
    for i in range(len(x)) :
        if x[i]%2 == 0 :
            return False 
            break
        else : pass
    return True

def no_odds(x) :
    for i in range(len(x)) :
        if x[i]%2 != 0 :
            return False
            break
        else : pass
    return True

def get_odds(x) :
    list = []
    for i in range(len(x)) :
        if x[i]%2 != 0 :
            list.append(x[i])
        else : pass
    return list

def zip_odds(a,b) :
    list_a = get_odds(a)
    list_b = get_odds(b)
    if len(list_b) > len(list_a) :
        list_all = [0]*(len(list_a)+len(list_b))
        i = 0
        n = len(list_a)
        m = 0
        while True :
            if n == 0 :
                break
            else : 
                list_all[i] = list_a[m]
                m +=1
                i +=2
                n -= 1
        a = 0
        for i in range(len(list_all)) :
            if list_all[i] != 0 :
                pass
            else :
                list_all[i] = list_b[a]
                a+=1
    elif len(list_b) < len(list_a) :
        list_all = [0]*(len(list_a)+len(list_b))
        i = 1
        n = len(list_b)
        m = 0
        while True :
            if n == 0 :
                break
            else : 
                list_all[i] = list_b[m]
                m +=1
                i +=2
                n -= 1
        a = 0
        for i in range(len(list_all)) :
            if list_all[i] != 0 :
                pass
            else :
                list_all[i] = list_a[a]
                a+=1    
    else : 
        list_all = []
        n_a = 0
        n_b = 0
        for i in range(len(list_a)+len(list_b)) :
            if i%2 == 0:
                list_all.append(list_a[n_a])
                n_a +=1
            else :
                list_all.append(list_b[n_b])
                n_b +=1
    return list_all    


exec(input().strip())