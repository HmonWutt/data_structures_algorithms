board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board_2=[[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
def sudoku_solver(board):
    if not is_empty(board):
        print_board(board)
        return True
    length = len(board)
    for row in range(length):
        for col in range(length):
            if is_cell_empty(board,row,col):
        
                for num in range(1,length+1):
                    if is_valid(num,board,row,col):
                        board[row][col] = str(num)
                        if sudoku_solver(board):
                            return True
                        board[row][col] = "."
                return False    
            

                
    return False

def is_empty(board):
    is_empty = False
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == ".":
                return True
    return is_empty
def is_cell_empty(board,row,col):
    return board[row][col] =="."

def is_valid(num,board,row,col):
    for r in range(len(board)):
        if board[r][col]==str(num):
            return False
        
    for c in range(len(board)):
        if board[row][c]==str(num):
            return False

    r = (row//3 )*3
    c = (col//3) *3
    for rr in range(r,r+3):
        for cc in range(c,c+3):
            if board[rr][cc] == str(num):
                return False
    return True


def print_board(board):
    for row in board:
        print(row)
    print()

sudoku_solver(board_2)

