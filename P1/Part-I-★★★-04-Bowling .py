def in_score(result) :
    list_score  = []   
    i = 0 
    while True :
        score = 0
        if len(list_score) == 9 and result[i] == "X" :
            if result[-2] == "X" :
                if result[-1] == "X" :
                    score = 30
                    list_score.append(score)
                else : 
                    score = 20
                    score += int(result[-1])
                    list_score.append(score)
            elif  result[-1] == "/" :
                score = 20
                list_score.append(score)
            else :
                score = 10
                score += int(result[-2])
                score += int(result[-1])
                list_score.append(score)
            break
        elif i == len(result)-3 and result[i+1] == "/" :
            if result[-1] == "X" :
                score = 20
                list_score.append(score)
            else : 
                score = 10
                score += int(result[-1])
                list_score.append(score)
            break
        elif i == len(result)-2 :
            score += int(result[-2])
            score += int(result[-1])
            list_score.append(score)
            break
        elif result[i] == "X" and result[i+1] == "X" :
            if result[i+2] == "X" :
                score = 30
                list_score.append(score)
            else : 
                score = 20
                score += int(result[i+2])
                list_score.append(score)
            i += 1
        elif result[i] == "X"  :
            if result[i+2] == "/" :
                score = 20
                list_score.append(score)
            else :
                score = 10
                score += int(result[i+1]) + int(result[i+2])
                list_score.append(score)
            i +=1
        elif result[i+1] == "/":
            if result[i+2] == "X" :
                    score = 20                 
                    list_score.append(score)
                    i +=2
            else :
                    score = 10
                    score += int(result[i+2])
                    list_score.append(score)
                    i +=2
        else :
            score += int(result[i]) + int(result[i+1])
            list_score.append(score)
            i+=2
    return list_score


result = input().strip()
target = input()
m = in_score(result)
list_number = ["1","2",'3','4','5','6','7','8','9','10']
if target in list_number :
    print(m[int(target)-1])
else :
    score = 0
    for i in range(len(m)) :
        score += m[i]
    print(score)









          
 





