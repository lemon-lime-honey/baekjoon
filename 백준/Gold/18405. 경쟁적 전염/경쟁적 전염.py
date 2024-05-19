from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tubes = list()
virus = list()

for i in range(n):
    tubes.append(list(map(int, input().split())))
    for j in range(n):
        if tubes[i][j] != 0:
            virus.append((tubes[i][j], i, j))

que = deque(x[1:] for x in sorted(virus, key=lambda x: x[0]))
s, x, y = map(int, input().split())
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

while s:
    m = len(que)
    for i in range(m):
        r, c = que.popleft()
        for j in range(4):
            nr, nc = r + dr[j], c + dc[j]
            if (nr < 0 or nc < 0 or
                nr >= n or nc >= n or
                tubes[nr][nc] != 0):
                continue
            tubes[nr][nc] = tubes[r][c]
            que.append((nr, nc))
    s -= 1

print(tubes[x - 1][y - 1])