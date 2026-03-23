def isSafe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n, print_flag):
    global count
    if row == n:
        count += 1
        if print_flag:
            for i in range(n):
                print(board[i])
            print()
        return

    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, print_flag)
            board[row][col] = 0


# Main
n = int(input("Enter value of n: "))
board = [[0]*n for _ in range(n)]
count = 0

# First pass → count only
solve(board, 0, n, False)
print("Total solutions:", count)

# Second pass → print solutions
count = 0
solve(board, 0, n, True)
