import string

pos = input().strip()
if len(pos) <= 3 :
    row = pos[0]
    col = pos[1:].strip()
else : 
    if pos[0] == 'r' :
        m,n = pos.split(',')
        row = m.split('=')[1].strip()
        col = n.split('=')[1].strip()
    if pos[0] == 'c' :
        m,n = pos.split(',')
        col = m.split('=')[1].strip()
        row = n.split('=')[1].strip()

# Valid row and column
valid_row = (len(row) == 1) and (row in string.ascii_letters)
n = 0
for i in range(len(col)) :
    if col[i] in string.digits :
        n += 1

if len(col) == 0 :
    valid_column = False
elif n == len(col) :
    if int(col) <= 52 and int(col) >= 1 :
        valid_column = True
    else :
        valid_column = False
else : 
    valid_column = False

# Output
if not valid_row and not valid_column :
    print('Invalid row and column')
elif not valid_row :
    print('Invalid row')
elif not valid_column :
    print('Invalid column')
else :
    if ord(row)%2 == 0 :
        if int(col)%2 == 0 :
            print('White')
        else :
            print('Black')
    else :
        if int(col)%2 == 0 :
            print('Black')
        else :
            print('White')