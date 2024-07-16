from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [int(1e9) for i in range(n + 1)]
dist[1] = 0

que = deque([(1, 0)])

while que:
    now, d = que.popleft()
    if dist[now] < d: continue
    for next_point in graph[now]:
        if dist[next_point] <= d + 1: continue
        dist[next_point] = d + 1
        que.append((next_point, d + 1))

res = sorted(zip(range(1, n + 1), dist[1:]), key=lambda x: (-x[1], x[0]))
result = [res[0][0], res[0][1], 1]

for i in range(1, n):
    if res[i][1] != result[1]: break
    result[2] += 1

print(*result)