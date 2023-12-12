from collections import deque

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

board = [[-1 for i in range(n)] for j in range(n)]
que = deque([(r1, c1)])
board[r1][c1] = 0

while que:
    r, c = que.popleft()

    for i in range(6):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
        if board[nr][nc] != -1: continue
        board[nr][nc] = board[r][c] + 1
        if nr == r2 and nc == c2: break
        que.append((nr, nc))

print(board[r2][c2])