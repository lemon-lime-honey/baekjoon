import heapq

n = int(input())
k = int(input())
censors = sorted(list(map(int, input().split())))
heap = list()
result = 0

for i in range(1, n):
    heapq.heappush(heap, censors[i] - censors[i - 1])

while len(heap) > k - 1:
    result += heapq.heappop(heap)

print(result)