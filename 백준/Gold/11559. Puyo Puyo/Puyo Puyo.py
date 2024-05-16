from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    chk = [[False for i in range(6)] for j in range(12)]
    blocks = list()

    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] != '.':
                que = deque([(i, j)])
                chk[i][j] = True
                temp = [(i, j)]
                while que:
                    r, c = que.popleft()
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if (nr < 0 or 12 <= nr or
                            nc < 0 or 6 <= nc or
                            board[nr][nc] != board[r][c] or
                            chk[nr][nc]):
                            continue
                        chk[nr][nc] = True
                        temp.append((nr, nc))
                        que.append((nr, nc))
                if len(temp) >= 4:
                    blocks.extend(temp)

    return blocks


def erase():
    for r, c in targets:
        board[r][c] = '.'


def fall():
    for i in range(6):
        for j in range(11, -1, -1):
            if board[j][i] != '.' and j != 11:
                ref = j
                idx = j + 1
                while idx < 12:
                    if board[idx][i] != '.':
                        break
                    board[idx][i], board[ref][i] = board[ref][i], board[idx][i]
                    idx += 1
                    ref += 1


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

board = [list(input().rstrip()) for i in range(12)]
result = 0

while True:
    targets = bfs()
    if not targets:
        print(result)
        break
    erase()
    fall()
    result += 1
