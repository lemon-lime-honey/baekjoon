from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(m)]
chk = [[False for i in range(n)] for j in range(m)]

dr = [0, 0, -1, 1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]

que = deque()
result = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and not chk[i][j]:
            que.append((i, j))
            chk[i][j] = True

            while que:
                r, c = que.popleft()
                for k in range(8):
                    nr, nc = r + dr[k], c + dc[k]
                    if (nr < 0 or nr >= m or
                        nc < 0 or nc >= n or
                        chk[nr][nc] or
                        graph[nr][nc] == 0):
                        continue
                    chk[nr][nc] = True
                    que.append((nr, nc))

            result += 1

print(result)