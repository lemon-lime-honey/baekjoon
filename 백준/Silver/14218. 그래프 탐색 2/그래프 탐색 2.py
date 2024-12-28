from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    que = deque([(1, 0)])

    while que:
        c, d = que.popleft()

        if dist[c] < d:
            continue

        for nc in routes[c]:
            nd = d + 1
            if dist[nc] < nd:
                continue
            dist[nc] = nd
            que.append((nc, nd))


n, m = map(int, input().split())
dist = [int(1e9) for i in range(n + 1)]
routes = [[] for i in range(n + 1)]

dist[1] = 0

for i in range(m):
    u, v = map(int, input().split())
    routes[u].append(v)
    routes[v].append(u)

q = int(input())

for i in range(q):
    u, v = map(int, input().split())
    routes[u].append(v)
    routes[v].append(u)
    bfs()

    for j in range(1, n + 1):
        if j == n:
            if dist[j] == int(1e9):
                print(-1)
            else:
                print(dist[j])
        else:
            if dist[j] == int(1e9):
                print(-1, end=" ")
            else:
                print(dist[j], end=" ")
