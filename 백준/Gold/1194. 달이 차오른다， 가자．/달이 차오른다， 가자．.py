from collections import deque
import sys

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
chk = [[[False for i in range(1 << 6)] for j in range(m)] for k in range(n)]
maze = list()
que = deque()
result = int(1e9)

for i in range(n):
    maze.append(input().rstrip())
    if not que:
        for j in range(m):
            if maze[i][j] == "0":
                que.append((i, j, 0, 0))
                chk[i][j][0] = True

while que:
    r, c, cnt, key = que.popleft()

    if maze[r][c] == "1":
        result = cnt
        break

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if (
            nr < 0
            or nc < 0
            or nr >= n
            or nc >= m
            or maze[nr][nc] == "#"
            or chk[nr][nc][key]
        ):
            continue
        nk = key

        if maze[nr][nc].isalpha():
            if maze[nr][nc].isupper() and not nk & 1 << ord(maze[nr][nc]) - ord("A"):
                continue
            elif maze[nr][nc].islower():
                nk |= 1 << ord(maze[nr][nc]) - ord('a')
                
        chk[nr][nc][key] = True
        que.append((nr, nc, cnt + 1, nk))

print(result if result != int(1e9) else -1)
