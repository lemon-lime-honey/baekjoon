import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
sight = list(map(int, input().split()))
result = [INF for i in range(n)]
graph = [[] for i in range(n)]
que = [(0, 0)]
result[0] = 0

for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    graph[b].append((t, a))

while que:
    cost, point = heapq.heappop(que)
    if result[point] < cost: continue

    for next_cost, next_point in graph[point]:
        if next_point != (n - 1) and sight[next_point]:
            continue
        if cost + next_cost < result[next_point]:
            result[next_point] = cost + next_cost
            heapq.heappush(que, (cost + next_cost, next_point))

print(-1 if result[-1] == INF else result[-1])