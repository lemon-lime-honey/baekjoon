from collections import deque

n = int(input())
graph = [False for i in range(n + 1)]
dist = [0] + list(map(int, input().split()))

start = int(input())

que = deque()
que.append(start)

while que:
    point = que.popleft()

    if point < 1 or point > n or graph[point]:
        continue

    graph[point] = True
    que.append(point + dist[point])
    que.append(point - dist[point])

print(graph.count(True))
