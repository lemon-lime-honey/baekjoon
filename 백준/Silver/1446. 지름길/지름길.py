import heapq, sys
input = sys.stdin.readline

n, d = map(int, input().split())
highway = [int(1e9) for i in range(d + 1)]
short = [[] for i in range(d + 1)]
que = list()

heapq.heappush(que, (0, 0))
highway[0] = 0

for i in range(n):
    s, e, l = map(int, input().split())
    if e > d: continue
    short[s].append((l, e))

for i in range(d):
    short[i].append((1, i + 1))

while que:
    dist, now = heapq.heappop(que)

    if highway[now] < dist: continue

    for length, end in short[now]:
        if highway[end] < dist + length: continue
        highway[end] = dist + length
        heapq.heappush(que, (highway[end], end))

print(highway[-1])