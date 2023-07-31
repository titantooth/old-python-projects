import math,random, pprint

def check_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c

    return None,None

def is_valid(puzzle, guess, row, col):
    #check rows
    val_rows = puzzle[row]
    if guess in val_rows:
        return False

    #check columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #check box

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row+3):
        for j in range(start_col, start_col+3):
            if puzzle[i][j]== guess:
                return False

    return True

def solve_sodoku(puzzle):
    row, col = check_next_empty(puzzle)
    if row == None:
        return True

    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sodoku(puzzle):
                return True

        puzzle[row][col] = -1

    return False
example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

print(solve_sodoku(example_board))
pprint.pprint(example_board)


