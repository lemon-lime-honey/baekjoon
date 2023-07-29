from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def melt(targets):
    global maps

    result = deepcopy(maps)
    for row, col in targets:
        que = deque([(row, col)])
        while que:
            r, c = que.popleft()
            cnt = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if (0 <= nr < n) and (0 <= nc < m) and not maps[nr][nc]:
                    cnt += 1
            if cnt:
                result[r][c] -= cnt
                if result[r][c] < 0: result[r][c] = 0

    maps = result


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(n)]
time = 0

while True:
    glacier = list()
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]
    chk = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j]:
                glacier.append((i, j))
                if not visited[i][j]:
                    que.append((i, j))
                    visited[i][j] = True
                    while que:
                        r, c = que.popleft()
                        for k in range(4):
                            nr, nc = r + dr[k], c + dc[k]
                            if (0 <= nr < n) and (0 <= nc < m):
                                if not visited[nr][nc] and maps[nr][nc]:
                                    visited[nr][nc] = True
                                    que.append((nr, nc))
                    chk += 1
    if not glacier:
        print(0)
        break
    if chk > 1:
        print(time)
        break
    time += 1
    melt(glacier)