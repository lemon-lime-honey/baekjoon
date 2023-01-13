import sys, heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    command = int(sys.stdin.readline())
    if command == 0:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -1 * command)