import sys

input = sys.stdin.readline


def find(c):
    if parent[c] != c:
        parent[c] = find(parent[c])
    return parent[c]


def union(c1, c2):
    c1, c2 = find(c1), find(c2)
    if c1 == c2:
        return False
    if c1 < c2:
        parent[c2] = c1
    else:
        parent[c1] = c2
    return True


n, p = map(int, input().split())
costs = [int(input()) for i in range(n)]
parent = [i for i in range(n + 1)]
graph = list()

for i in range(p):
    s, e, l = map(int, input().split())
    graph.append((2 * l + costs[s - 1] + costs[e - 1], s, e))

graph.sort()
result = 0

for l, s, e in graph:
    if union(s, e):
        result += l

print(result + min(costs))
