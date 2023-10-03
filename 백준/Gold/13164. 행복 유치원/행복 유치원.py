import heapq

n, k = map(int, input().split())
heights = list(map(int, input().split()))
heap = list()
result = 0

for i in range(1, n):
    heapq.heappush(heap, heights[i] - heights[i - 1])

while len(heap) > k - 1:
    result += heapq.heappop(heap)

print(result)