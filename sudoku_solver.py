board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def sudoku_solver(board):
    if not is_empty(board):
        return board
    length = len(board)
    for row in range(length):
        for col in range(length):
            for num in range(1,length+1):
                if is_valid(num,board,row,col):
                    board[row][col] = num
                    return sudoku_solver(board)
            board[row][col] = "."
            return
    return "not solvable"

def is_empty(board):
    is_empty = False
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == ".":
                return True
    return is_empty

def is_valid(num,board,row,col):
    for r in range(len(board)):
        if r!=row and board[row][col]==num:
            return False
        
    for c in range(col,len(board)):
        if c!=col and board[row][c]==num:
            return False

    r = row//3
    c = col//3
    for rr in range(r,r+3):
        for cc in range(c,c+3):
            if rr!=row and cc!=col and board[rr][cc] == num:
                return False
    return False


    

sudoku_solver(board)

