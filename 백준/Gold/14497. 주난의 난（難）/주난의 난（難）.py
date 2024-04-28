from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
chk = [[0 for i in range(m)] for j in range(n)]
maps = list()
target = None
start = None

for i in range(n):
    maps.append(list(input().rstrip()))
    for j in range(m):
        if maps[i][j] == '*':
            start = (i, j)
        elif maps[i][j] == '#':
            target = (i, j)

chk[start[0]][start[1]] = 1
que = deque()
que.append(start)

while que:
    r, c = que.popleft()
    if r == target[0] and c == target[1]:
        print(chk[r][c] - 1)
        break
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 > nr or nr >= n or 0 > nc or nc >= m or chk[nr][nc] != 0:
            continue
        if maps[nr][nc] == '0':
            chk[nr][nc] = chk[r][c]
            que.appendleft((nr, nc))
        elif maps[nr][nc] != '0':
            chk[nr][nc] = chk[r][c] + 1
            que.append((nr, nc))