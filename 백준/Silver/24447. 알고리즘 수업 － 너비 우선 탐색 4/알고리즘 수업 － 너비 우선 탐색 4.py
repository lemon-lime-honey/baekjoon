from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())
depth = [-1 for i in range(n + 1)]
graph = [[] for i in range(n + 1)]
order = [0 for i in range(n + 1)]
que = deque([r])
depth[r] = 0
result = 0
ref = 0

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
    graph[v].sort()

while que:
    now = que.popleft()

    if not order[now]:
        ref += 1
        order[now] = ref

        for element in graph[now]:
            if depth[element] == -1:
                que.append(element)
                depth[element] = depth[now] + 1

for i in range(1, n + 1):
    result += depth[i] * order[i]

print(result)