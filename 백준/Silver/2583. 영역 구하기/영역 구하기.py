from collections import deque
import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(y, x):
    global cnt
    que = deque([[y, x]])

    while que:
        ty, tx = map(int, que.popleft())
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and not space[ny][nx]:
                space[ny][nx] = 2
                cnt += 1
                que.append([ny, nx])

m, n, k = map(int, sys.stdin.readline().split())
space = [[0 for i in range(n)] for j in range(m)]
div = 0
area = list()

for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for j in range(y1, y2):
        for l in range(x1, x2):
            space[j][l] = 1

for i in range(m):
    for j in range(n):
        if not space[i][j]:
            space[i][j] = 2
            cnt = 1
            div += 1
            bfs(i, j)
            area.append(cnt)

area.sort()

print(div)
print(*area)