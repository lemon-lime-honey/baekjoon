knight = [-1, -1]
first = [-1, -1]
board = [[False for i in range(6)] for j in range(6)]
flag = True

dr = [-2, -1, -2, -1, 2, 1, 2, 1]
dc = [-1, -2, 1, 2, -1, -2, 1, 2]

for i in range(36):
    ipt = input()
    if flag:
        r = 6 - int(ipt[1])
        c = ord(ipt[0]) - ord('A')
        if knight[0] == -1:
            knight = [r, c]
            first = [r, c]
            board[r][c] = True
        else:
            for j in range(8):
                nr, nc = knight[0] + dr[j], knight[1] + dc[j]
                if nr == r and nc == c and not board[nr][nc]:
                    board[nr][nc] = True
                    knight = [nr, nc]
                    break
            else:
                flag = False

if flag:
    for i in range(8):
        nr, nc = knight[0] + dr[i], knight[1] + dc[i]
        if nr == first[0] and nc == first[1]:
            break
    else:
        flag = False

if flag:
    for i in range(6):
        if flag:
            for j in range(6):
                if not board[i][j]:
                    flag = False
                    break
        else:
            break
    

print('Valid' if flag else 'Invalid')