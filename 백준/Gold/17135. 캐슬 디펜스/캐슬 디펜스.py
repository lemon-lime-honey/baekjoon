from collections import deque
from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
archers = combinations(range(m), 3)
mvmt = [(0, -1), (-1, 0), (0, 1)]
result = 0

for archer in archers:
    temp = 0
    board_now = deepcopy(board)
    for i in range(n - 1, -1, -1):
        enemy = set()
        for j in archer:
            que = deque([(i, j, 1)])
            while que:
                r, c, k = que.popleft()
                if board_now[r][c] == 1:
                    enemy.add((r, c))
                    break
                if k < d:
                    for dr, dc in mvmt:
                        nr, nc = r + dr, c + dc
                        if 0 > nr or 0 > nc or nc >= m:
                            continue
                        que.append((nr, nc, k + 1))
        temp += len(enemy)
        for ni, nj in enemy:
            board_now[ni][nj] = 0
    result = max(result, temp)

print(result)