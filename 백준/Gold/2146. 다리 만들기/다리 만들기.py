from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline


def bfs(row, col, target):
    que = deque([(row, col)])
    maps[row][col] = target

    while que:
        r, c = que.popleft()
        cnt = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (nr < 0 or nc < 0 or
                nr >= n or nc >= n or
                maps[nr][nc] == target):
                continue
            if maps[nr][nc] == 0:
                cnt += 1
                continue
            maps[nr][nc] = target
            que.append((nr, nc))
        if cnt != 0:
            edges.add((r, c))


def bridge(row, col, chk):
    global result
    que = deque([(row, col, 0)])
    _map = deepcopy(maps)
    
    while que:
        r, c, dist = que.popleft()
        if _map[r][c] >= result: continue
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (nr < 0 or nc < 0 or
                nr >= n or nc >= n or
                _map[nr][nc] == chk or
                _map[nr][nc] > 0):
                continue
            if _map[nr][nc] < 0:
                result = min(result, dist)
                return
            _map[nr][nc] = dist + 1
            que.append((nr, nc, dist + 1))


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n = int(input())
maps = [list(map(int, input().split())) for i in range(n)]

edges = set()
result = int(1e9)
num = -1

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            bfs(i, j, num)
            num -= 1

for row, col in edges:
    bridge(row, col, maps[row][col])

print(result)