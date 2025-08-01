class SudokuSolver:
    def __init__(self, board):
        self.board = [row[:] for row in board]  # Create a copy
        self.size = 9
        self.box_size = 3
    
    def solve(self):
        """Main solving method using backtracking"""
        empty_cell = self._find_empty_cell()
        if not empty_cell:
            return True  # No empty cells means puzzle is solved
        
        row, col = empty_cell
        
        for num in range(1, 10):
            if self._is_valid_move(num, row, col):
                self.board[row][col] = num
                
                if self.solve():  # Recursive call
                    return True
                
                self.board[row][col] = 0  # Backtrack
        
        return False  # No solution found
    
    def _find_empty_cell(self):
        """Find the next empty cell (returns None if board is complete)"""
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    return (row, col)
        return None
    
    def _is_valid_move(self, num, row, col):
        """Check if placing num at (row, col) is valid"""
        return (self._check_row(num, row) and 
                self._check_column(num, col) and 
                self._check_box(num, row, col))
    
    def _check_row(self, num, row):
        """Check if num already exists in the row"""
        return num not in self.board[row]
    
    def _check_column(self, num, col):
        """Check if num already exists in the column"""
        return num not in [self.board[row][col] for row in range(self.size)]
    
    def _check_box(self, num, row, col):
        """Check if num already exists in the 3x3 box"""
        box_row = (row // self.box_size) * self.box_size
        box_col = (col // self.box_size) * self.box_size
        
        for i in range(box_row, box_row + self.box_size):
            for j in range(box_col, box_col + self.box_size):
                if self.board[i][j] == num:
                    return False
        return True
    
    def print_board(self):
        """Pretty print the board with grid lines"""
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("------+-------+------")
            
            row_str = ""
            for j, cell in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += "| "
                row_str += f"{cell if cell != 0 else '.'} "
            print(row_str)
    
    def get_solution(self):
        """Return the solved board"""
        return self.board


# Example usage
def solve_sudoku(puzzle, show_steps=True):
    """Convenient function to solve a sudoku puzzle"""
    solver = SudokuSolver(puzzle)
    
    if show_steps:
        print("Original puzzle:")
        solver.print_board()
        print("\nSolving...\n")
    
    if solver.solve():
        if show_steps:
            print("Solution found:")
            solver.print_board()
        return solver.get_solution()
    else:
        print("No solution exists for this puzzle!")
        return None


# Test puzzles
easy_puzzle = [
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

hard_puzzle = [
    [0, 0, 0, 6, 0, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 8, 0, 0, 0, 3],
    [0, 0, 0, 3, 0, 6, 0, 4, 5],
    [0, 4, 0, 2, 0, 0, 0, 6, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 1, 0, 0]
]

# Solve the easy puzzle
solution = solve_sudoku(easy_puzzle)

print("\n" + "="*30)
print("Hard puzzle:")
solve_sudoku(hard_puzzle)