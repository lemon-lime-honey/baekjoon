import sys

input = sys.stdin.readline


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
    else:
        parent[p] = q


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    union(u, v)

timetable = list(map(int, input().split()))
result = 0

for i in range(1, n):
    if find(timetable[i - 1]) != find(timetable[i]):
        result += 1

print(result)
