from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(int, input().strip())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if room[i][j]: room[i][j] = 0
        else: room[i][j] = int(1e9)

que = deque([[0, 0]])
room[0][0] = 1

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

while que:
    r, c = que.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if (0 <= nr < n) and (0 <= nc < n):
            if room[nr][nc] == 0:
                room[nr][nc] = room[r][c]
                que.appendleft([nr, nc])
            elif (room[r][c] + 1 < room[nr][nc]):
                room[nr][nc] = room[r][c] + 1
                que.append([nr, nc])

print(room[-1][-1] - 1)