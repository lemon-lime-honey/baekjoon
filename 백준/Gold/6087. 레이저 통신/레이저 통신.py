from collections import deque
import sys
input = sys.stdin.readline

w, h = map(int, input().split())
que = deque()
maps = list()
target = None

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[[int(1e9)] * 4 for i in range(w)] for j in range(h)]

for i in range(h):
    maps.append(list(input().rstrip()))
    for j in range(w):
        if maps[i][j] == 'C':
            if not que:
                for k in range(4):
                    que.append((i, j, k, 0))
                    visited[i][j][k] = 0
            else:
                target = (i, j)

while que:
    r, c, d, m = que.popleft()
    for i in range(4):
        nr, nc = r + direction[i][0], c + direction[i][1]
        if (0 > nr or nr >= h or
            0 > nc or nc >= w or
            visited[nr][nc][i] <= m or
            maps[nr][nc] == '*'):
            continue
        if i == d:
            visited[nr][nc][i] = m
            que.append((nr, nc, i, m))
        else:
            if visited[nr][nc][i] < m + 1:
                continue
            visited[nr][nc][i] = m + 1
            que.append((nr, nc, i, m + 1))

print(min(visited[target[0]][target[1]]))