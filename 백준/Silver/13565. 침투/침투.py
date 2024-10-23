from collections import deque
import sys

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

m, n = map(int, input().split())
maps = [list(map(int, list(input().rstrip()))) for i in range(m)]

que = deque()
result = False

for i in range(n):
    if maps[0][i] == 0:
        que.append((0, i))
        maps[0][i] = 2

while que:
    r, c = que.popleft()

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 > nr or 0 > nc or nr >= m or nc >= n or maps[nr][nc] != 0:
            continue

        maps[nr][nc] = 2
        que.append((nr, nc))

for i in range(n):
    if maps[m - 1][i] == 2:
        result = True
        break

print("YES" if result else "NO")
