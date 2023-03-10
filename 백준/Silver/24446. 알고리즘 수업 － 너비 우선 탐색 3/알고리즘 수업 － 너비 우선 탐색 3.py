from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())
result = [-1 for i in range(n + 1)]
graph = [[] for i in range(n + 1)]
result[r] = 0
que = deque([r])

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

while que:
    now = que.popleft()

    for element in graph[now]:
        if result[element] == -1:
            que.append(element)
            result[element] = result[now] + 1

for i in range(1, n + 1):
    print(result[i])