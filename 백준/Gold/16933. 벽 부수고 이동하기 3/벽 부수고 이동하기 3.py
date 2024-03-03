from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
maps = [list(map(int, list(input().rstrip()))) for i in range(n)]
visited = [[[int(1e9) for i in range(k + 1)] for j in range(m)] for l in range(n)]
que = deque([(0, 0, 0, 1, 0)])
visited[0][0][0] = 1

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

while que:
    r, c, wall, dist, night = que.popleft()

    if visited[r][c][wall] < dist: continue

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
        if maps[nr][nc] == 1 and wall < k:
            if night == 0 and dist + 1 < visited[nr][nc][wall + 1]:
                visited[nr][nc][wall + 1] = dist + 1
                que.append((nr, nc, wall + 1, dist + 1, 1))
            elif (night == 1 and dist + 2 < visited[nr][nc][wall + 1]):
                visited[nr][nc][wall + 1] = dist + 2
                que.append((nr, nc, wall + 1, dist + 2, 1))
        elif (maps[nr][nc] == 0 and dist + 1 < visited[nr][nc][wall]):
            visited[nr][nc][wall] = dist + 1
            que.append((nr, nc, wall, dist + 1, 1 if night == 0 else 0))

result = min(visited[n - 1][m - 1])
print(-1 if result == int(1e9) else result)