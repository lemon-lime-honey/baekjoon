import heapq, sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
roads = [[] for i in range(n + 1)]
result = [[] for i in range(n + 1)]
res = list()

for i in range(m):
    a, b, c = map(int, input().split())
    roads[a].append((b, c))

que = [(0, 1)]
heapq.heappush(result[1], 0)

while que:
    time, now = heapq.heappop(que)
    for next_point, next_time in roads[now]:
        if len(result[next_point]) < k:
            heapq.heappush(result[next_point], -(time + next_time))
            heapq.heappush(que, (time + next_time, next_point))
        elif -result[next_point][0] > time + next_time:
            heapq.heappop(result[next_point])
            heapq.heappush(result[next_point], -(time + next_time))
            heapq.heappush(que, (time + next_time, next_point))

for i in range(1, n + 1):
    if len(result[i]) < k:
        res.append(-1)
    else:
        res.append(-result[i][0])

print(*res, sep='\n')