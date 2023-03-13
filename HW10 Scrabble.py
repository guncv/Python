# Scrabble by TA Touchy, revised by TA Son

########## DONT EDIT BELOW THIS LINE #####################

# import longdict.txt to colab
import os
os.rename("uc?id=1wo9dqhnUmm_WJam3oue60nN8KzAjOy-L","longdict.txt")

# Implement get_value(letter) function for students
letter_value = {'a':1 , 'b':3, 'c':3, 'd':2, 'e':1, 'f':4,
                'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,
                'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,
                's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

def get_value(letter):
    if letter.lower() in letter_value:
        return letter_value[letter.lower()]
    return -1

# Get word_list from text file
dic = open("longdict.txt","r")

word_list = set()
for line in dic:
    word_list.add(line.strip())

# Implement is_valid(word) for students to use
def is_valid(word):
    if len(word)>=2 and (word.upper() in word_list):
        return True
    return False

# Implement make_board() for students to use
def make_board():
    board = []
    for i in range(15):
        board.append(['']*15)
    return board

# Implement copy_board(board) for students to use
def copy_board(board):
    new_board = []
    for i in range(15):
        new_board.append(list(board[i]))
    return new_board

# Implement print_board(board) for students to use
# Print board to terminal
def print_board(board):
    top = "   "
    for i in range(0,15):
        # Top numbers
        top += " "*max(0,3-len(str(i))) + str(i) + " "
    print(top)
    for i in range(len(board)):
        # Side numbers
        line = str(i)+" "*max(0,3-len(str(i)))+""
        
        for j in range(len(board)):
            if board[i][j]=="":
                if i==7 and j==7:
                    line += "  * "
                else:
                    line += "  _ "
            else:
                line += " ["+str(board[i][j])+"]"
        print(line)
    print()

# Implement place_tiles(row,col,down,tiles,board) for students to use
# place tiles on the board without checking anything
def place_tiles(row,col,down,tiles,board):
    # Trying to place on occupied block
    if board[row][col]!="":
        return [False,board]    
    new_board = copy_board(board)
    start = False
    connect = False
    # Check if game started
    if board[7][7]!="":
        start = True
    r=row
    c=col
    tiles = tiles.upper()
    placed = 0
    # If go down
    if down:
        if (row-1>=0 and board[row-1][col]!="") or (row+len(tiles)<=14 and board[row+len(tiles)][col]!=""):
            connect=True
        while placed<len(tiles):
            if r>14:
                #print(88)
                return [False,board]
            # that block is empty
            if new_board[r][c]=="":
                new_board[r][c]=tiles[placed]
                # Check connect left or right
                if c-1>=0 and new_board[r][c-1]!="":
                    connect = True
                if c+1<=14 and new_board[r][c+1]!="":
                    connect = True
                placed+=1
                r+=1
            # that block is NOT empty
            else:
                connect = True
                r+=1
    # If left to right
    else:
        if (col-1>=0 and board[row][col-1]!="") or (col+len(tiles)<=14 and board[row][col+len(tiles)]!=""):
            connect=True
        while placed<len(tiles):
            if c>14:
                return [False,board]
            # that block is empty
            if new_board[r][c]=="":
                new_board[r][c]=tiles[placed]
                # Check connect above or below
                if r-1>=0 and new_board[r-1][c]!="":
                    connect = True
                if r+1<=14 and new_board[r+1][c]!="":
                    connect = True
                placed+=1
                c+=1
            # that block is NOT empty
            else:
                connect = True
                c+=1
    if (not start and new_board[7][7]=="") or (start and not connect):
        #print(124,start,connect)
        return [False,board]
    return [True, new_board]

########## DONT EDIT ABOVE THIS LINE #####################