import sys
input = sys.stdin.readline


def puzzle(n):
    if n == len(zeros):
        for i in range(9):
            print(*board[i])
        sys.exit()

    number = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    r, c = zeros[n]
    row, col = r // 3, c // 3

    for i in range(row * 3, (row + 1) * 3):
        for j in range(col * 3, (col + 1) * 3):
            if board[i][j] in number:
                number.remove(board[i][j])

    for i in range(9):
        if board[r][i] in number:
            number.remove(board[r][i])
        if board[i][c] in number:
            number.remove(board[i][c])

    for num in number:
        board[r][c] = num
        puzzle(n + 1)
    
    board[r][c] = 0


board = list()
zeros = list()

for i in range(9):
    board.append(list(map(int, input().split())))
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))

puzzle(0)