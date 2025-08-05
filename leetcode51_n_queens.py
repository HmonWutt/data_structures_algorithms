def n_queens(num,count,row, new_board):
    board = []
    if count == num:
        temp = [",".join(i) for i in new_board]
        board.append(temp)
        print(new_board)
        return board 
    if row > num-1:
        return board
    for col in range(len(new_board)):
        
        if is_valid(row,col,new_board):
            new_board[row][col]= "Q"
            
            board+=n_queens(num,count+1,row+1,new_board)
            new_board[row][col] ="."
    return board


def is_valid(row,col,board):
    r = row
    if row>0:
        while r >0:
            if board[r-1][col]=="Q":
                return False
            r-=1
        r1 = row
        c = col
        while r1 >0 and c+1 <len(board):
            if board[r1-1][c+1] == "Q":
                return False
            r1-=1
            c+=1
        
        count = min(row,col)
        for _ in range(count):
            if board[row-1][col-1] == "Q":
                return False
            row-=1
            col-=1
    return True
def print_board(board):
    for row in board:
        print(row)
    print()
num = 4
new_board =[ ["."] * num for i in range (num)]
print(n_queens(4,0,0,new_board))