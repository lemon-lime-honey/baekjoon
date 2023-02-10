import sys
from collections import deque

def bfs(start):
    visited = [True] + [False] * n
    result = [0] * (n + 1)
    que = deque([start])
    cnt = 0

    while que:
        now = que.popleft()

        if not visited[now]:
            cnt += 1
            visited[now] = True
            result[now] = cnt
            for element in link[now]:
                que.append(element)
    
    return result

n, m, r = map(int, sys.stdin.readline().split())
link = [[] for i in range(n + 1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    link[u].append(v)
    link[v].append(u)

for i in range(1, n + 1):
    link[i].sort(reverse = True)

visited = [True] + [False] * (n)
route = bfs(r)

for i in range(1, n + 1):
    print(route[i])