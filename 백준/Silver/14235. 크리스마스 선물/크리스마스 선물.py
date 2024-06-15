import heapq, sys
input = sys.stdin.readline

n = int(input())
present = list()

for i in range(n):
    ipt = list(map(int, input().split()))
    if ipt[0] == 0:
        print(-heapq.heappop(present) if present else -1)
    else:
        for p in ipt[1:]:
            heapq.heappush(present, -p)
