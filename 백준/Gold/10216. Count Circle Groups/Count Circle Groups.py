import math, sys
input = sys.stdin.readline


def find(p):
    if parent[p] != p:
        parent[p] = find(parent[p])
    return parent[p]


def union(p, q):
    p, q = find(p), find(q)
    if p < q:
        parent[q] = p
    else:
        parent[p] = q


t = int(input())

for i in range(t):
    n = int(input())
    parent = [i for i in range(n)]
    data = [list(map(int, input().split())) for i in range(n)]

    for j in range(n - 1):
        for k in range(j + 1, n):
            dist = math.sqrt(
                (data[j][0] - data[k][0]) ** 2 + (data[j][1] - data[k][1]) ** 2
            )
            if data[j][2] + data[k][2] < dist or find(j) == find(k):
                continue
            union(j, k)

    for j in range(n):
        find(j)

    print(len(set(parent)))
