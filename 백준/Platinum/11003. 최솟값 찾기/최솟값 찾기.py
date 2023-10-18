import heapq, sys
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
result = [0 for i in range(n)]
heap = list()

for i in range(n):
    heapq.heappush(heap, (a[i], i))

    while heap[0][1] < i - l + 1:
        heapq.heappop(heap)

    result[i] = heap[0][0]

print(*result)