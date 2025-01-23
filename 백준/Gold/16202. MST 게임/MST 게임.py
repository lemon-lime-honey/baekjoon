import sys

input = sys.stdin.readline


def get_mst():
    result = 0
    target = -1

    for i, (w, u, v) in enumerate(graph):
        if i in indices:
            continue

        if union(u, v):
            result += w
            if target == -1:
                target = i

    for i in range(2, n + 1):
        if find(i) != parent[i - 1]:
            return 0

    indices.add(target)

    return result


def find(p):
    if p != parent[p]:
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


n, m, k = map(int, input().split())
graph = list()

for i in range(m):
    x, y = map(int, input().split())
    graph.append((i + 1, x, y))

graph.sort()

result = list()
indices = set()

for i in range(k):
    parent = [i for i in range(n + 1)]
    result.append(get_mst())

print(*result)
