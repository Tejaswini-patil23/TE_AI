def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


def solve(row, n, cols, diag1, diag2, board, count, print_flag, path=""):
    if row == n:
        count[0] += 1
        print(path + "✔ SOLUTION FOUND")
        print_board(board)
        return

    for col in range(n):

        print(path + f"🔍 Trying ({row},{col})")

        # BOUND (pruning)
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            print(path + f"✂ PRUNED ({row},{col}) - not safe")
            continue

        print(path + f"✔ Placing queen at ({row},{col})")

        # choose
        board[row][col] = 1
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        print(path + "📌 Current board:")
        print_board(board)

        # explore branch
        solve(row + 1, n, cols, diag1, diag2, board, count, print_flag, path + "  ")

        # backtrack
        print(path + f"↩ Removing queen from ({row},{col})")

        board[row][col] = 0
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

        print(path + "📌 Board after backtracking:")
        print_board(board)


n = 4
board = [[0]*n for _ in range(n)]
count = [0]

solve(0, n, set(), set(), set(), board, count, False)

print("TOTAL SOLUTIONS:", count[0])
