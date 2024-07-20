import heapq, sys
input = sys.stdin.readline


def find(p):
    if cities[p] == p: return p
    cities[p] = find(cities[p])
    return cities[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q: return False
    if p < q: cities[q] = p
    else: cities[p] = q
    return True


n, m, t = map(int, input().split())
cities = [i for i in range(n + 1)]
road = list()
result = 0
cnt = 0

for i in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(road, (c, a, b))

while road:
    cost, a, b = heapq.heappop(road)
    if union(a, b):
        result += cost
        cnt += 1

for i in range(cnt - 1):
    result += (i + 1) * t

print(result)
