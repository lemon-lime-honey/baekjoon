import heapq, sys
input = sys.stdin.readline

n = int(input())
stations = sorted([list(map(int, input().split())) for i in range(n)],
                  key=lambda x: (x[0], -x[1]))

l, p = map(int, input().split())
stations.append((l, 0))
heap = list()
result = 0

for dist, fuel in stations:
    if p >= l: break
    while p < dist and heap:
        p -= heapq.heappop(heap)
        result += 1
    if p < dist: break
    heapq.heappush(heap, -fuel)

print(result if p >= l else -1)