import random

def is_valid(board, row, col):
    # Check if a queen can be placed at the given position
    for i in range(row):
        if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
            return False
    return True

def solve_n_queens(n):
    board = [-1] * n
    queens_placed = 0

    while queens_placed < n:
        # Randomly select a column for the next queen in the remaining rows
        col = random.randint(0, n - 1)

        if is_valid(board, queens_placed, col):
            board[queens_placed] = col
            queens_placed += 1

    return board


n = 8
solution = solve_n_queens(n)

# Print the solution
for row in solution:
    line = ['Q' if col == row else '.' for col in range(n)]
    print(' '.join(line))
