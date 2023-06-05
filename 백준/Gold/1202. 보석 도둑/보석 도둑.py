import heapq, sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = list()
jewel = list()
total = 0

for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))

bags = [int(input()) for i in range(k)]
bags.sort()

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(jewel, -heapq.heappop(jewels)[1])
    if jewel: total -= heapq.heappop(jewel)
    elif not jewels: break

print(total)