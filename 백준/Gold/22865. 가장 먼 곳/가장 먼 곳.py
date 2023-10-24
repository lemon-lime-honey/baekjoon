import heapq, sys
input = sys.stdin.readline


def dijkstra(house):
    dist[house] = 0

    que = [(0, house)]

    while que:
        cost, now = heapq.heappop(que)

        if dist[now] < cost: continue

        for next_point, next_cost in roads[now]:
            if dist[next_point] < dist[now] + next_cost: continue
            dist[next_point] = dist[now] + next_cost
            heapq.heappush(que, (cost + next_cost, next_point))


n = int(input())
houses = list(map(int, input().split()))
m = int(input())
roads = [[] for i in range(n + 1)]

for i in range(m):
    d, e, l = map(int, input().split())
    roads[d].append((e, l))
    roads[e].append((d, l))

result = [int(1e9) for i in range(n + 1)]

for i in range(3):
    dist = [int(1e9) for i in range(n + 1)]
    dijkstra(houses[i])

    for i in range(1, n + 1):
        result[i] = min(result[i], dist[i])

answer = [-1, 0]

for i in range(1, n + 1):
    if answer[0] < result[i]:
        answer[0] = result[i]
        answer[1] = i

print(answer[1])