import heapq, sys
input = sys.stdin.readline


def find(p):
    if p != group[p]:
        group[p] = find(group[p])
    return group[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q: return False
    if p < q: group[q] = p
    else: group[p] = q
    return True


n, m, k = map(int, input().split())
raw_costs = list(map(int, input().split()))
group = [i for i in range(n + 1)]
costs = list()
result = 0

for i in range(n):
    heapq.heappush(costs, (raw_costs[i], i + 1))

for i in range(m):
    v, w = map(int, input().split())
    if v != w:
        union(v, w)

while costs:
    cost, number = heapq.heappop(costs)
    if union(0, number):
        result += cost

for i in range(1, n + 1):
    chk = find(i)
    if chk:
        print('Oh no')
        break
else:
    print(result if result <= k else 'Oh no')