import sys
from collections import deque
input = sys.stdin.readline

graph = [[0 for i in range(501)] for j in range(501)]
n = int(input())

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(min(x1, x2), max(x1, x2) + 1):
        for k in range(min(y1, y2), max(y1, y2) + 1):
            graph[j][k] = 1

m = int(input())

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(min(x1, x2), max(x1, x2) + 1):
        for k in range(min(y1, y2), max(y1, y2) + 1):
            graph[j][k] = 2

que = deque([[0, 0]])
graph[0][0] = 3

while que:
    x, y = que.popleft()
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if (0 <= nx < 501) and (0 <= ny < 501):
            if graph[nx][ny] == 2: continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                que.appendleft([nx, ny])
            elif graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                que.append([nx, ny])

print(graph[-1][-1] - 3 if graph[-1][-1] > 2 else -1)