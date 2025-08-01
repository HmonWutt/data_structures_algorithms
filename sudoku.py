def sudoku_solver(board):
    if is_not_empty(board):
        print("complete")
        print_board(board)
        return True
    for row in range(9):
        for col in range(9):
            #print("row: ",row,"col: ",col)
            if is_empty(row,col,board):   
                for num in range(1,10):
                    if is_valid(num,row,col,board):  
                        board[row][col] = num

                    #print_board(board)
                        if sudoku_solver(board):
                            return True            
                    #print("undo")       
                        board[row][col] = 0
                    #print_board(board)
                return False
        

    return False


def is_valid(num,row,col,board):
    for each_row in board:
        if each_row[col]==num:
            return False
    for c in range(len(board)):
        if board[row][c] == num:
            return False
    start_row = row-(row%3)
    start_col = col - (col%3)
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if board[i][j] == num:
                return False
    return True
                               

def is_not_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def is_empty(row,col,board):
    return board[row][col]==0

def print_board(board):
    for each in board:
        print(each)
    print()
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

board = [
    [5, 3, 0, 6, 7, 8, 9, 1, 2],
    [6, 0, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 3],
    [4, 2, 6, 8, 0, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 0, 8, 5, 6],
    [0, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 0, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 0, 7]
]

sudoku_solver(sudoku_board)


