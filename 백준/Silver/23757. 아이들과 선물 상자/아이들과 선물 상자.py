import heapq

n, m = map(int, input().split())
c = list(map(int, input().split()))
w = list(map(int, input().split()))
p = list()

for i in range(n):
    heapq.heappush(p, -c[i])

for i in range(m):
    if -p[0] < w[i]:
        print(0)
        break
    heapq.heappush(p, -(-heapq.heappop(p) - w[i]))
else:
    print(1)
