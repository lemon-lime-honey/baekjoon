import heapq, sys

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    command = int(sys.stdin.readline())
    if command > 0:
        heapq.heappush(heap, command)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)