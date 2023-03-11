import sys

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
depth = [-1] * (n + 1)
stack = [[r, 0]]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse = True)

while stack:
    now, d = stack.pop()

    if not visited[now]:
        visited[now] = True
        depth[now] = d

        for element in graph[now]:
            if not visited[element]:
                stack.append([element, d + 1])

print(*depth[1:], sep='\n')