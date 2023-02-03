import heapq

n, k = map(int, input().split())
number = list(map(int, input().split()))
heap = list()

for i in range(n):
    heapq.heappush(heap, number.pop())

for i in range(k):
    if i == (k - 1):
        print(heapq.heappop(heap))
    else:
        heapq.heappop(heap)