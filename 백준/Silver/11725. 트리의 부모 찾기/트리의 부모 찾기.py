import sys
from collections import deque

def bfs():
    que = deque(([1]))
    while que:
        now = que.popleft()
        for point in link[now]:
            if not parent[point] and point != 1:
                parent[point] = now
                que.append(point)

n = int(sys.stdin.readline())
link = [[] for i in range(n + 1)]
parent = [0] * (n + 1)

for i in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    link[u].append(v)
    link[v].append(u)

bfs()
print(*parent[2:], sep = '\n')