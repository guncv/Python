dict_mark = {"R":1,"Y":2,"G":3,"W":4,"B":5,"P":6,"K":7}
red = 6
player1 = 0
player2 = 0
m = 6
while m > 0 :
    x = input()
    if red > 0 :
        if x[0] == "1" :
            if x[1] == "R" :
                player1 += 1
                red -= 1
                if x[2] in dict_mark :
                    player1 += dict_mark[x[2]]
            else : pass
        elif x[0] == "2" :
            if x[1] == "R" :
                player2 += 1
                red -= 1
                if x[2] in dict_mark :
                    player2 += dict_mark[x[2]]
            else : pass
    else :
        if x[0] == "1" :
            if x[1] in dict_mark :
                player1 += dict_mark[x[1]]
                m -= 1
            else : pass
        elif x[0] == "2" :
            if x[1] in dict_mark :
                player2 += dict_mark[x[1]]
                m -= 1
            else : pass
print(str(player1),str(player2))
if player1 > player2 :
    print("Player 1 wins")
elif player1 < player2 :
    print("Player 2 wins")
else : print("Tie")


        
