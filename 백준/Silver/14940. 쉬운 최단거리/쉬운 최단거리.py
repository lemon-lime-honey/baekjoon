from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

n, m = map(int, input().split())
result = [[-1 for i in range(m)] for j in range(n)]
graph = list()
que = deque()

for i in range(n):
    ipt = list(map(int, input().split()))
    graph.append(ipt)
    for j in range(m):
        if ipt[j] == 2:
            result[i][j] = 0
            que.append((i, j))
            break

while que:
    r, c = que.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if (0 <= nr < n) and (0 <= nc < m) and result[nr][nc] == -1:
            if graph[nr][nc] == 0: result[nr][nc] = 0
            else:
                result[nr][nc] = result[r][c] + 1
                que.append((nr, nc))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and result[i][j] == -1:
            result[i][j] = 0

for i in range(n):
    print(*result[i])