from collections import deque
import sys
input = sys.stdin.readline


def bfs(row, col):
    que = deque([(row, col)])
    chk[row][col] = True
    cnt = 1

    while que:
        r, c = que.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < m and
                0 <= nc < n and
                not chk[nr][nc] and
                maps[nr][nc] == maps[row][col]):
                que.append((nr, nc))
                chk[nr][nc] = True
                cnt += 1

    return cnt


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
maps = [input().rstrip() for i in range(m)]
chk = [[False for i in range(n)] for j in range(m)]
result = [0, 0]

for i in range(m):
    for j in range(n):
        if not chk[i][j]:
            if maps[i][j] == 'W':
                result[0] += bfs(i, j) ** 2
            else:
                result[1] += bfs(i, j) ** 2

print(*result)