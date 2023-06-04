def is_safe(board, row, col, N):
    # Check if there is any queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queen(board, row, N):
    # Base case: all queens have been placed
    if row == N:
        print_board(board)
        return True

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen in the current position
            board[row][col] = 1

            # Recur to place the queens in the next row
            if solve_n_queen(board, row + 1, N):
                return True

            # Backtrack: remove the queen from the current position
            board[row][col] = 0

    return False


def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()


def n_queen(N):
    board = [[0] * N for _ in range(N)]
    solve_n_queen(board, 0, N)


n_queen(8)
