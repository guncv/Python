def operator_R(DNA) :
    old = "ACGT"
    new = "TGCA"
    m = ""
    for i in range(len(DNA)) :
        if DNA[i] in old :
            in_dex = old.index(DNA[i])
            m += new[in_dex]            
        else : pass
    return m[::-1]

def operator_D(DNA) :
    s = input()
    x = 0
    for i in range(len(DNA)) :
        if i == len(DNA)-1 :
            break
        if DNA[i:i+2] == s :
            x +=1
    return x

def operator_F(DNA) :
    list_DNA = ["A","T","G","C"]
    A = 0
    T = 0
    G = 0
    C = 0
    for i in DNA : 
        if i == "A" :
            A += 1
        elif i == "T" :
            T += 1
        elif i == "G" :
            G += 1
        else :
            C += 1
    m = "A"+"="+str(A)+",","T"+"="+str(T)+",","G"+"="+str(G)+",","C"+"="+str(C)
    return " ".join(m)

def invalid_DNA(DNA) :
    s = "useful"
    list = "ATGC"
    for i in DNA :
        if i in list : pass
        else : 
            s = "useless"
            break
    return s
      
                    
DNA = input().strip()
operator = input()
DNA = DNA.upper()
s = invalid_DNA(DNA)
if s == "useful" :
    if operator == "R" :
        print(operator_R(DNA))
    if operator == "D" :
        print(operator_D(DNA))
    if operator == "F" :
        print(operator_F(DNA))
else : print("Invalid DNA")

        
