import sys

input = sys.stdin.readline


def find(p):
    if parent[p] != p:
        parent[p] = find(parent[p])
    return parent[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q:
        return False
    if p < q:
        parent[q] = p
    else:
        parent[p] = q
    return True


n = int(input())
graph = list()

for i in range(n - 1):
    ipt = list(map(int, input().split()))
    for j in range(len(ipt)):
        graph.append((ipt[j], i + 1, i + j + 2))

graph.sort()
result = [[] for i in range(n + 1)]
parent = [i for i in range(n + 1)]

for w, u, v in graph:
    if union(u, v):
        result[u].append(v)
        result[v].append(u)

for i in range(1, n + 1):
    result[i].sort()

for i in range(1, n + 1):
    print(len(result[i]), *result[i])
