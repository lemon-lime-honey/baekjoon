from collections import deque
import sys

dr = [0, 0, 1, 0, 0, -1]
dc = [0, 1, 0, 0, -1, 0]
dh = [1, 0, 0, -1, 0, 0]

m, n, h = map(int, sys.stdin.readline().split())
box = [[[0 for i in range(m)] for j in range(n)] for k in range(h)]
points = list()
que = deque()
result = 0

for i in range(h):
    for j in range(n):
        box[i][j] = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if box[i][j][k] == 1:
                que.append([i, j, k])

while que:
    hei, row, col = que.popleft()

    for i in range(6):
        nh = hei + dh[i]
        nr = row + dr[i]
        nc = col + dc[i]
        
        if (0 <= nh < h) and (0 <= nr < n) and (0 <= nc < m) and not box[nh][nr][nc]:
            box[nh][nr][nc] = box[hei][row][col] + 1
            que.append([nh, nr, nc])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if not box[i][j][k]:
                print(-1)
                exit()
            if result < box[i][j][k]:
                result = box[i][j][k]

print(result - 1)