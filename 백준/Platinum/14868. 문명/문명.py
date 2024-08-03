from collections import deque
import sys
input = sys.stdin.readline


def find(p):
    if parent[p] == p:
        return p
    parent[p] = find(parent[p])
    return parent[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q:
        return False
    if p < q:
        parent[q] = p
    else:
        parent[p] = q
    return True


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, k = map(int, input().split())
parent = [i for i in range(k + 1)]
maps = [[0 for i in range(n)] for j in range(n)]
que = deque()
result = 0

for i in range(1, k + 1):
    x, y = map(int, input().split())
    maps[x - 1][y - 1] = i
    que.append((x - 1, y - 1))

m = len(que)

for i in range(m):
    r, c = que.popleft()
    for j in range(4):
        nr, nc = r + dr[j], c + dc[j]
        if nr < 0 or nc < 0 or nr >= n or nc >= n or maps[nr][nc] == 0:
            continue
        if union(maps[nr][nc], maps[r][c]):
            k -= 1
    que.append((r, c))

while k != 1 and que:
    result += 1
    m = len(que)
    for i in range(m):
        r, c = que.popleft()
        for j in range(4):
            nr, nc = r + dr[j], c + dc[j]
            if (
                nr < 0
                or nc < 0
                or nr >= n
                or nc >= n
                or maps[nr][nc] == maps[r][c]
                or find(maps[nr][nc]) == find(maps[r][c])
            ):
                continue

            if maps[nr][nc] == 0:
                maps[nr][nc] = maps[r][c]
                for l in range(4):
                    nnr, nnc = nr + dr[l], nc + dc[l]
                    if (
                        nnr < 0
                        or nnc < 0
                        or nnr >= n
                        or nnc >= n
                        or maps[nnr][nnc] == maps[nr][nc]
                        or maps[nnr][nnc] == 0
                        or find(maps[nnr][nnc]) == find(maps[nr][nc])
                    ):
                        continue
                    if union(maps[nnr][nnc], maps[r][c]):
                        k -= 1
            elif union(maps[nr][nc], maps[r][c]):
                k -= 1
            que.append((nr, nc))

print(result)
