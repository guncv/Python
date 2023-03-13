number_card = ["A","2","3","4","5","6","7" \
    ,"8","9","T","J","Q","K"]
score_card = [1,2,3,4,5,6,7,8,9,10,11,12,13]
type_card = ["C","D","H","S"]
score_type = [1,2,3,4]
input_card = input()
output_card = []
i = 0
while True :
    if i == (len(input_card)-2) :
        break
    else :
        if input_card[i] != input_card[i+2] :
            n1 = score_card[number_card.index(input_card[i])]
            n2 = score_card[number_card.index(input_card[i+2])]
            different = n1-n2
            if different > 0 :
                output_card.append("+"+str(different))
            else :
                output_card.append(str(different))
        else :
            m1 = score_type[type_card.index(input_card[i+1])]
            m2 = score_type[type_card.index(input_card[i+3])]
            different = m1-m2
            if different > 0 :
                output_card.append("+"+str(different))
            else :
                output_card.append(str(different))
        i += 2
print("".join(output_card))