n = int(input())
board = [list(input()) for i in range(n)]
click = [list(input()) for i in range(n)]
result = [['.' for i in range(n)] for j in range(n)]
exp = False

dr = [0, 0, -1, 1, -1, 1, -1, 1]
dc = [1, -1, 0, 0, -1, 1, 1, -1]

for i in range(n):
    for j in range(n):
        if click[i][j] == 'x':
            if board[i][j] == '*':
                result[i][j] = '*'
                exp = True
            else:
                chk = 0
                for k in range(8):
                    nr, nc = i + dr[k], j + dc[k]
                    if (0 <= nr < n) and (0 <= nc < n) and board[nr][nc] == '*':
                        chk += 1
                result[i][j] = str(chk)

if exp:
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*' and result[i][j] != '*':
                result[i][j] = '*'

for i in range(n):
    print(''.join(result[i]))