import sys
input = sys.stdin.readline


def find(p):
    if parent[p] != p:
        parent[p] = find(parent[p])
    return parent[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q:
        return
    parent[p] = q


n, m, k = map(int, input().split())
cards = sorted(list(map(int, input().split())))
opponent = list(map(int, input().split()))
parent = [i for i in range(n)]
result = list()

for card in opponent:
    lo, hi = 0, m - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if cards[mid] <= card:
            lo = mid + 1
        else:
            hi = mid - 1
    while cards[lo] <= card:
        lo += 1
    target = find(lo)
    result.append(cards[target])
    union(target, target + 1)

print(*result, sep='\n')