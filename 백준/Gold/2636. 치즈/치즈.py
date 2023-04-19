from collections import deque


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs():
    que = deque()
    que.append([0, 0])
    visited[0][0] = True
    cnt = 0
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < n) and (0 <= nc < m) and not visited[nr][nc]:
                if cheese[nr][nc] == 0:
                    visited[nr][nc] = True
                    que.append([nr, nc])
                else:
                    visited[nr][nc] = True
                    cheese[nr][nc] = 0
                    cnt += 1
    cnts.append(cnt)
    return cnt


n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for i in range(n)]
cnts = list()
time = 0

while True:
    visited = [[False for i in range(m)] for j in range(n)]
    cnt = bfs()
    if not cnt: break
    time += 1

print(time, cnts[-2], sep='\n')