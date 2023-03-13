x = input()
sentence = input()
list = ['"',"(",")",",",".","'"," "]
l =[]
for i in range(len(sentence)) :
    n = len(x)
    if i == len(sentence)-n+1 :
        break
    elif i == len(sentence)-n :
        if sentence[i-1] in list :
            l.append(sentence[i:])
        else : pass
    elif i == 0 :
        if sentence[n] in list :
            l.append(sentence[0:n])
        else : pass
    else :
        if sentence[i-1] in list and sentence[i+n] in list :
            l.append(sentence[i:n])
        else : pass
print(l)


    
      