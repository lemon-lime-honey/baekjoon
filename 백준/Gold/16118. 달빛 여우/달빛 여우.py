import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d * 2))
    graph[b].append((a, d * 2))

fox = [1e9 for i in range(n + 1)]
fox[1] = 0
que = [(0, 1)]

while que:
    dist, point = heapq.heappop(que)

    if fox[point] < dist: continue

    for next_point, next_dist in graph[point]:
        if fox[next_point] > dist + next_dist:
            fox[next_point] = dist + next_dist
            heapq.heappush(que, (dist + next_dist, next_point))

wolf = [[1e9, 1e9] for i in range(n + 1)]
wolf[1][0] = 0
que = [(0, 1, 0)]

while que:
    dist, point, speed = heapq.heappop(que)

    if wolf[point][speed] < dist: continue

    if speed:
        for next_point, next_dist in graph[point]:
            chk = dist + next_dist * 2
            if wolf[next_point][0] > chk:
                wolf[next_point][0] = chk
                heapq.heappush(que, (chk, next_point, 0))
    else:
        for next_point, next_dist in graph[point]:
            chk = dist + next_dist / 2
            if wolf[next_point][1] > chk:
                wolf[next_point][1] = chk
                heapq.heappush(que, (chk, next_point, 1))

result = 0

for i in range(1, n + 1):
    if fox[i] < min(wolf[i]): result += 1

print(result)