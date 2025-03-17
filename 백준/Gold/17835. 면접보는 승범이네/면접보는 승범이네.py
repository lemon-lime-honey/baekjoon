import heapq, sys


def dijkstra():
    hq = list()
    
    for city in cities:
        heapq.heappush(hq, (0, city))
        distance[city] = 0

    while hq:
        dist, point = heapq.heappop(hq)
        if distance[point] < dist:
            continue
        for next_point, next_dist in graph[point]:
            if distance[next_point] <= dist + next_dist:
                continue
            distance[next_point] = dist + next_dist
            heapq.heappush(hq, (dist + next_dist, next_point))


input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v, c = map(int, input().split())
    graph[v].append((u, c))

distance = [float('inf') for i in range(n + 1)]
result = [float('inf') for i in range(n + 1)]

cities = list(map(int, input().split()))

dijkstra()

for j in range(1, n + 1):
    if distance[j] < result[j]:
        result[j] = distance[j]

answer = [float('inf'), -1]

for i in range(1, n + 1):
    if distance[i] < answer[1] or (distance[i] == answer[1] and answer[0] < i):
        continue
    answer[0] = i
    answer[1] = distance[i]

print(answer[0])
print(answer[1])
