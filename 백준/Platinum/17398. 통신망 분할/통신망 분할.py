import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(p):
    if parent[p] == p:
        return p
    parent[p] = find(parent[p])
    return parent[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q:
        return
    if p < q:
        parent[q] = p
        size[p] += size[q]
    else:
        parent[p] = q
        size[q] += size[p]


n, m, q = map(int, input().split())
link = [list(map(int, input().split())) for i in range(m)]
targets = [False for i in range(m)]
parent = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]
queries = list()
result = 0

for i in range(q):
    queries.append(int(input()) - 1)
    targets[queries[-1]] = True

for i in range(m):
    if targets[i]: continue
    union(link[i][0], link[i][1])

for i in range(q - 1, -1, -1):
    a, b = find(link[queries[i]][0]), find(link[queries[i]][1])
    if a != b:
        cnt = [0, 0]
        result += size[a] * size[b]
        union(a, b)

print(result)
