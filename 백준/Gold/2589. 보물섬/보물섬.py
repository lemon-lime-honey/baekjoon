from collections import deque
import sys
input = sys.stdin.readline


def bfs(row, col):
    global result

    chk = [[-1 for i in range(m)] for j in range(n)]
    que = deque([(row, col, 0)])
    chk[row][col] = 0

    while que:
        r, c, dist = que.popleft()
        if chk[r][c] < dist:
            continue
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < n and
                0 <= nc < m and
                maps[nr][nc] == 'L' and
                chk[nr][nc] == -1):
                chk[nr][nc] = dist + 1
                que.append((nr, nc, dist + 1))

    result = max(result, max(map(max, chk)))


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
maps = [input().rstrip() for i in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'L':
            bfs(i, j)

print(result)