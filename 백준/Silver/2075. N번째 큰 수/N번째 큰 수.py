import sys, heapq

n = int(sys.stdin.readline())
heap = list()

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if len(heap) < 2 * n:
            heapq.heappush(heap, temp[j])
        else:
            if heap[0] < temp[j]:
                heapq.heappop(heap)
                heapq.heappush(heap, temp[j])

for i in range(len(heap) - n):
    heapq.heappop(heap)

print(heap[0])