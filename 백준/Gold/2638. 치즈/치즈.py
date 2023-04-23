from collections import deque


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs():
    que = deque()
    que.append([0, 0])
    visited[0][0] = True
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < n) and (0 <= nc < m) and not visited[nr][nc]:
                if cheese[nr][nc] == 0:
                    visited[nr][nc] = True
                    que.append([nr, nc])
                else:
                    cheese[nr][nc] += 1


n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for i in range(n)]
time = 0

while True:
    visited = [[False for i in range(m)] for j in range(n)]
    chk = False
    bfs()
    for i in range(n):
        for j in range(m):
            if cheese[i][j] > 2:
                cheese[i][j] = 0
            elif cheese[i][j] > 0:
                cheese[i][j] = 1
                chk = True
    time += 1
    if not chk: break

print(time)