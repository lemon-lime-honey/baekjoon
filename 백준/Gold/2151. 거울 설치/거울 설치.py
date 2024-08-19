from collections import deque
import sys

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n = int(input())
house = list()
que = deque()
door = list()
mirror_cnt = 0
chk = [[[int(1e9) for i in range(4)] for j in range(n)] for k in range(n)]

for i in range(n):
    house.append(input().rstrip())
    for j in range(n):
        match house[i][j]:
            case "#":
                door.append((i, j))
            case "!":
                mirror_cnt += 1

for i in range(4):
    nr, nc = door[0][0] + dr[i], door[0][1] + dc[i]
    if nr < 0 or nc < 0 or nr >= n or nc >= n or house[nr][nc] == "*":
        continue
    que.append((door[0][0], door[0][1], i, 0))
    chk[door[0][0]][door[0][1]][i] = 0

while que:
    r, c, d, m = que.popleft()
    if chk[r][c][d] < m:
        continue
    r += dr[d]
    c += dc[d]

    while 0 <= r < n and 0 <= c < n:
        if chk[r][c][d] < m or house[r][c] == "*":
            break
        chk[r][c][d] = m
        match house[r][c]:
            case "!":
                if d in (0, 1):
                    que.append((r, c, 2, m + 1))
                    que.append((r, c, 3, m + 1))
                elif d in (2, 3):
                    que.append((r, c, 0, m + 1))
                    que.append((r, c, 1, m + 1))
            case "#":
                break
        r += dr[d]
        c += dc[d]

print(min(chk[door[1][0]][door[1][1]]))
