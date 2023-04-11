from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
maze = [list(map(int, input().strip())) for i in range(n)]
maze[0][0] = 2
que = deque([[0, 0]])

while que:
    r, c = que.popleft()
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r + dr, c + dc
        if (0 <= nr < n) and (0 <= nc < m):
            if maze[nr][nc] == 0:
                maze[nr][nc] = maze[r][c]
                que.appendleft([nr, nc])
            elif maze[nr][nc] == 1:
                maze[nr][nc] = maze[r][c] + 1
                que.append([nr, nc])

print(maze[n - 1][m - 1] -  2)