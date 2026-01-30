def solve():
    board = [input() for i in range(8)]

    row = set()
    col = set()
    diag1 = set()
    diag2 = set()

    for i in range(8):
        for j in range(8):
            if board[i][j] == "*":
                if i in row or j in col or i - j in diag1 or i + j in diag2:
                    print("invalid")
                    return
                row.add(i)
                col.add(j)
                diag1.add(i - j)
                diag2.add(i + j)

    if len(row) != 8:
        print("invalid")
    else:
        print("valid")

    return


solve()
