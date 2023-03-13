def is_prime(n) :
    if n <= 1 :
        return False
    for i  in range(2,int(n**0.5)+1) :
        if n%i == 0 :
            return False 
    return True

def next_prime (N) :
    N +=1 
    while not is_prime(N) :
        N +=1
    return N

def next_twin_prime(n) :
    n +=1 
    while not is_prime(n) or not is_prime(n+2) :
        n +=1 
    return n,n+2
        
exec(input().strip())