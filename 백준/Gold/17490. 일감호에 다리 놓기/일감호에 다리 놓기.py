import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def find(p):
    if p != road[p]:
        road[p] = find(road[p])
    return road[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q:
        return False
    if p < q:
        road[q] = p
    else:
        road[p] = q
    return True


n, m, k = map(int, input().split())
stone = [0] + list(map(int, input().split()))
road = [i for i in range(n + 1)]
erased = set()
cost = dict()

for i in range(m):
    a, b = map(int, input().split())
    erased.add((min(a, b), max(a, b)))

if m <= 1:
    print("YES")
    sys.exit()


for i in range(1, n + 1):
    u, v = i, i + 1

    if v == n + 1:
        u, v = 1, i

    if (u, v) not in erased:
        union(u, v)

for i in range(1, n + 1):
    target = find(i)
    chk = stone[i]
    cost[target] = min(cost.get(target, 1_000_001), chk)

if sum(cost.values()) <= k:
    print("YES")
else:
    print("NO")
