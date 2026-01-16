def solve_n_queens(n):
    cols = set()
    diag1 = set()   # row - col
    diag2 = set()   # row + col
    result = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row] = col

            backtrack(row + 1)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


# DISPLAY RESULT
print(solve_n_queens(4))