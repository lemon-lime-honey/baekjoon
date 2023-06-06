from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(v):
    que = deque()
    visited = [[-1 for i in range(n)] for j in range(n)]

    for r, c in v:
        que.append((r, c))
        visited[r][c] = 0
    
    time = 0
    chk = 0

    while que:
        r, c = que.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < n) and (0 <= nc < n):
                if not lab[nr][nc] and visited[nr][nc] == -1:
                    que.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                    time = max(time, visited[nr][nc])
                elif lab[nr][nc] == 2 and visited[nr][nc] == -1:
                    que.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                chk += 1
    
    if wall == chk:
        return time
    else:
        return int(1e9)


n, m = map(int, input().split())
virus = list()
lab = list()
wall = 0

for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(n):
        if lab[i][j] == 2:
            virus.append((i, j))
        elif lab[i][j] == 1:
            wall += 1

virus = list(combinations(virus, m))
result = int(1e9)

for v in virus:
    result = min(result, bfs(v))

print(-1 if result == int(1e9) else result)