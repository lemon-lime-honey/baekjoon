from collections import deque
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
    else:
        parent[p] = q


n, q = map(int, input().split())
parent = [i for i in range(n + 1)]
lst = [0 for i in range(n + 1)]

for i in range(2, n + 1):
    lst[i] = int(input())

queries = [list(map(int, input().split())) for i in range(n - 1 + q)]
result = deque()

for i in range(len(queries) - 1, -1, -1):
    if queries[i][0] == 0:
        union(queries[i][1], lst[queries[i][1]])
    else:
        if find(queries[i][1]) == find(queries[i][2]):
            result.appendleft("YES")
        else:
            result.appendleft("NO")

print(*result, sep="\n")
