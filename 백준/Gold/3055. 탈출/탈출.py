from collections import deque
import sys
input = sys.stdin.readline


def flood():
    n = len(water)
    for i in range(n):
        r, c = water.popleft()
        for j in range(4):
            nr, nc = r + dr[j], c + dc[j]
            if (0 <= nr < row and 0 <= nc < col and
                maps[nr][nc] == '.'):
                maps[nr][nc] = '*'
                water.append((nr, nc))
                


def bfs():
    que = deque([(start[0], start[1], 0)])
    visited = [[False for i in range(col)] for j in range(row)]
    visited[start[0]][start[1]] = True

    while que:
        flood()
        n = len(que)
        for i in range(n):
            r, c, m = que.popleft()
            for j in range(4):
                nr, nc = r + dr[j], c + dc[j]
                if (0 <= nr < row and 0 <= nc < col and
                    maps[nr][nc] in '.D' and not visited[nr][nc]):
                    if maps[nr][nc] == 'D':
                        return m + 1
                    visited[nr][nc] = True
                    que.append((nr, nc, m + 1))

    return -1


dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

row, col = map(int, input().split())
water = deque()
start = [0, 0]
maps = list()

for i in range(row):
    maps.append(list(input().rstrip()))
    for j in range(col):
        if maps[-1][j] == 'S':
            start = [i, j]
        if maps[-1][j] == '*':
            water.append((i, j))

result = bfs()
print(result if result != -1 else 'KAKTUS')