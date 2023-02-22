from collections import deque
import sys

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

m, n = map(int, sys.stdin.readline().split())
box = [[0 for j in range(m)] for k in range(n)]
points = list()
que = deque()
result = 0

for j in range(n):
    box[j] = list(map(int, sys.stdin.readline().split()))
    for k in range(m):
        if box[j][k] == 1:
            que.append([j, k])

while que:
    row, col = que.popleft()

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if (0 <= nr < n) and (0 <= nc < m) and not box[nr][nc]:
            box[nr][nc] = box[row][col] + 1
            que.append([nr, nc])

for j in range(n):
    for k in range(m):
        if not box[j][k]:
            print(-1)
            exit()
        if result < box[j][k]:
            result = box[j][k]

print(result - 1)