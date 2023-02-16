from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs(r, c):
    que = deque([[r, c]])

    while que:
        row, col = que.pop()
        chk[row][col] = True
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if (0 <= nr < n) and (0 <= nc < m) and not chk[nr][nc]:
                if (i < 2):
                    if (floor[row][col] == floor[nr][nc] == '-'):
                        chk[nr][nc] = True
                        que.appendleft([nr, nc])
                else:
                    if (floor[row][col] == floor[nr][nc] == '|'):
                        chk[nr][nc] = True
                        que.appendleft([nr, nc])

n, m = map(int, input().split())
chk = [[False for i in range(m)] for j in range(n)]
floor = list()
result = 0

for i in range(n):
    floor.append(list(input()))

for i in range(n):
    for j in range(m):
        if not chk[i][j]:
            chk[i][j] = True
            bfs(i, j)
            result += 1

print(result)