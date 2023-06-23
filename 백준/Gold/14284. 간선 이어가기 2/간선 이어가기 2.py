import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

s, t = map(int, input().split())
dist = [int(1e9) for i in range(n + 1)]
que = [(0, s)]
dist[s] = 0

while que:
    cost, point = heapq.heappop(que)
    for next_cost, next_point in graph[point]:
        if cost + next_cost < dist[next_point]:
            dist[next_point] = cost + next_cost
            heapq.heappush(que, (cost + next_cost, next_point))

print(dist[t])