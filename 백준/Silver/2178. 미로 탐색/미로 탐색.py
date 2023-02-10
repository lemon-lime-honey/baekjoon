import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    que = deque([(0, 0)])

    while que:
        now = que.popleft()

        for i in range(4):
            del_x = now[0] + dx[i]
            del_y = now[1] + dy[i]
            if (0 <= del_x < n) and (0 <= del_y < m):
                if maze[del_x][del_y] == 1:
                    maze[del_x][del_y] = maze[now[0]][now[1]] + 1
                    que.append((del_x, del_y))

n, m = map(int, sys.stdin.readline().split())
maze = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    maze[i] = list(map(int, sys.stdin.readline().strip()))

bfs()
print(maze[n - 1][m - 1])