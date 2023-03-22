from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [int(1e9) for i in range(200001)]
graph[n] = 0
que = deque([n])

while que:
    now = que.popleft()

    if 2 * now < 200001:
        if graph[now] < graph[2 * now]:
            graph[2 * now] = graph[now]
            que.appendleft(2 * now)
    if 0 <= (now - 1) < 200001:
        if graph[now] + 1 < graph[now - 1]:
            graph[now - 1] = graph[now] + 1
            que.append(now - 1)
    if 0 <= (now + 1) < 200001:
        if graph[now] + 1 < graph[now + 1]:
            graph[now + 1] = graph[now] + 1
            que.append(now + 1)

print(graph[k])