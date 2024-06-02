import heapq, sys
input = sys.stdin.readline


def find(p):
    if water[p] != p:
        water[p] = find(water[p])
    return water[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q: return False
    if p < q: water[q] = p
    else: water[p] = q
    return True


n = int(input())
water = [i for i in range(n + 1)]
heap = list()
result = 0

for i in range(n):
    heapq.heappush(heap, (int(input()), i + 1, 0))

for i in range(n):
    ipt = list(map(int, input().split()))
    for j in range(n):
        if i == j: continue
        heapq.heappush(heap, (ipt[j], i + 1, j + 1))

while heap:
    cost, a, b = heapq.heappop(heap)
    if union(a, b): result += cost

print(result)