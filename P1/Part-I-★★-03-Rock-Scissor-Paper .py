def rock_paper_scissor(x,y) :
    if x == "R" and y == "P" :
        return "Player2 win"
    elif x == "R" and y == "S" :
        return "Player1 win"
    elif x == "S" and y == "R" :
        return "Player2 win" 
    elif x == "S" and y == "P" :
        return "Player1 win"
    elif x == "P" and y == "S" :
        return "Player2 win"
    elif x == "P" and y == "P" :
        return "Tie"
    elif x == "S" and y == "S" :
        return "Tie"
    elif x == "R" and y == "R" :
        return "Tie"
    else : return "Player1 win"


m = int(input())
mark1 = 0
mark2 = 0
n = 0
while n < 3*m :
    x,y = input().split(" ")
    ans = rock_paper_scissor(x,y)
    if ans == "Player1 win" :
        mark1 +=1
    elif  ans == "Player2 win" :
        mark2 +=1
    else : pass
    if mark1 == m or mark2 == m :
        print(mark1,mark2)
        if mark1 > mark2 : print("Player 1 wins")
        else : print("Player 2 wins")
        break
    else : n +=1
if n == 3*m :
    print(mark1,mark2)
    print("Tie") 