def total(pocket) :
    total = 0
    for i in pocket :
        total += i*pocket[i]
    return total

def take(pocket,money_in) :
    for i in money_in :
        if i in pocket : pocket[i] += money_in[i]
        else : pocket[i] = money_in[i]
    return pocket

def pay(pocket,amt) :
    d,a ={},amt
    if amt > total(pocket) : return {}
    else :
         for key in sorted(pocket)[::-1]:
            if (a // key) * key >= pocket[key]*key :
                paid = key*pocket[key]
                a -= paid
                d[key] = paid//key
            elif (a // key) * key > 0 :
                paid = (a // key) * key
                a -= paid
                d[key] = paid//key
    if a > 0 : return {}
    else : 
        for i in d:
            pocket[i] -= d[i]
        return d


  
        




        

exec(input().strip())