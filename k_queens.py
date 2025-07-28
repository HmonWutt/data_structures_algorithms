def place_queens(row,board,queens):
    boards = []
    if queens == 4:
        temp_row = []
        for i in board:
            temp_col = []
            for j in i:
                temp_col.append(j)
            temp_row.append(temp_col)
        print()
        boards+=[temp_row]


        return boards
    if row == len(board):
        return []
    for col in range(len(board)):
        if is_valid(row,col,board):
            board[row][col]="Q"
            boards+=place_queens(row+1,board,queens+1)
            board[row][col]="X"
    return boards

def is_valid(row,col,board):
    r = row
    c = col
    for i in range(row):
        if board[i][col]=="Q":
            return False
    limit = min(row,col)
    for i in range(limit):
        if board[row-1][col-1] == "Q":
            return False
        row-=1
        col-=1
    limit = len(board)-c-1
    for i in range(limit):
        if board[r-1][c+1] == "Q":
            return False
        r-=1
        c+=1
    return True


board = [['X' for x in range(4)] for i in range(4)]
boards = place_queens(0,board,0)
for i in boards:
    for j in i:
        print(j)
    print()


