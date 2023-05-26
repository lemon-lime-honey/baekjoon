import sys
input = sys.stdin.readline


def puzzle(n):
    if n == len(zeros):
        for i in range(9):
            print(*board[i], sep='')
        sys.exit()
    
    r, c = zeros[n]
    row, col = r // 3, c // 3
    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for i in range(3 * row, (row + 1) * 3):
        for j in range(3 * col, (col + 1) * 3):
            if board[i][j] in nums:
                nums.remove(board[i][j])
    
    for i in range(9):
        if board[i][c] in nums:
            nums.remove(board[i][c])
        if board[r][i] in nums:
            nums.remove(board[r][i])
    
    for num in sorted(list(nums)):
        board[r][c] = num
        puzzle(n + 1)
    
    board[r][c] = 0


board = list()
zeros = list()

for i in range(9):
    board.append(list(map(int, input().strip())))
    for j in range(9):
        if board[-1][j] == 0:
            zeros.append((i, j))

puzzle(0)