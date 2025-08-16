from collections import defaultdict
import sys

input = sys.stdin.readline


def find(p):
    if p != cow[p]:
        cow[p] = find(cow[p])
    return cow[p]


def union(p, q):
    p, q = find(p), find(q)

    if p < q:
        cow[q] = p
    else:
        cow[p] = q


n, m = map(int, input().split())
cow = [i for i in range(n)]

coord = [list(map(int, input().split())) for i in range(n)]
group = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

for i in range(n):
    parent = find(i)
    group[parent].append(i)

result = int(1e9)

for indices in group.values():
    target = [int(1e9), int(1e9), 0, 0]
    for idx in indices:
        target[0] = min(target[0], coord[idx][0])
        target[1] = min(target[1], coord[idx][1])
        target[2] = max(target[2], coord[idx][0])
        target[3] = max(target[3], coord[idx][1])
    result = min(result, 2 * (abs(target[2] - target[0]) + abs(target[3] - target[1])))

print(result)
