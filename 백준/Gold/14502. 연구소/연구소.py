from collections import deque
from copy import deepcopy
import sys

def wall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if not original_map[i][j]:
                original_map[i][j] = 1
                wall(wall_cnt + 1)
                original_map[i][j] = 0

def bfs():
    wall_map = deepcopy(original_map)
    que = deque()

    for i in range(n):
        for j in range(m):
            if wall_map[i][j] == 2:
                que.append((i, j))
    
    while que:
        r, c = que.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if (0 <= nr < n) and (0 <= nc < m) and not wall_map[nr][nc]:
                wall_map[nr][nc] = 2
                que.append((nr, nc))
    
    global result
    cnt = 0

    for i in range(n):
        for j in range(m):
            if not wall_map[i][j]:
                cnt += 1
    
    result = max(cnt, result)

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, sys.stdin.readline().split())
original_map = [[] for i in range(n)]
result = 0

for i in range(n):
    original_map[i] = list(map(int, sys.stdin.readline().split()))

wall(0)
print(result)