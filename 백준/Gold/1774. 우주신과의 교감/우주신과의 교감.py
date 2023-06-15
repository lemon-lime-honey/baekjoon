from math import sqrt
import sys
input = sys.stdin.readline


def find(g):
    if g != god[g]:
        god[g] = find(god[g])
    return god[g]


def union(g1, g2):
    g1, g2 = find(g1), find(g2)
    if g1 == g2: return True
    if g1 <= g2: god[g2] = g1
    else: god[g1] = g2
    return False


n, m = map(int, input().split())
coord = [[0]] + [list(map(int, input().split())) for i in range(n)]
god = [i for i in range(n + 1)]
paths = list()
result = 0

for i in range(m):
    x, y = map(int, input().split())
    union(x, y)

for i in range(1, n):
    for j in range(i + 1, n + 1):
        if find(i) == find(j): continue
        dist = sqrt((coord[i][0] - coord[j][0]) ** 2 + (coord[i][1] - coord[j][1]) ** 2)
        paths.append((dist, i, j))

paths.sort()

for d, a, b in paths:
    chk = union(a, b)
    if not chk:
        result += d

print(f'{result:.2f}')