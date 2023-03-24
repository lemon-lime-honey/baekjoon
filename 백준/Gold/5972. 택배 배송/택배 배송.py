import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
result = [int(1e9) for i in range(n)]
cow = [[] for i in range(n)]
que = [(0, 0)]

for i in range(m):
    a, b, c = map(int, input().split())
    cow[a - 1].append((c, b - 1))
    cow[b - 1].append((c, a - 1))

while que:
    cost, point = heapq.heappop(que)

    for next_cost, next_point in cow[point]:
        if cost + next_cost < result[next_point]:
            result[next_point] = cost + next_cost
            heapq.heappush(que, (cost + next_cost, next_point))

print(result[-1])