from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def find(p):
    if p != group[p]:
        group[p] = find(group[p])
    return group[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q:
        return False
    if p < q:
        group[q] = p
    else:
        group[p] = q
    return True


n, m = map(int, input().split())
s, e = map(int, input().split())

group = [i for i in range(n + 1)]
bridge = list()

for i in range(m):
    h1, h2, k = map(int, input().split())
    bridge.append((k, h1, h2))

bridge.sort(reverse=True)
graph = [[] for i in range(n + 1)]

for k, h1, h2 in bridge:
    if union(h1, h2):
        graph[h1].append((h2, k))
        graph[h2].append((h1, k))

chk = [False for i in range(n + 1)]
que = deque([(s, int(1e9))])
chk[s] = True
result = 0

while que:
    now, weight = que.popleft()

    if now == e:
        result = weight
        break

    for next_point, next_weight in graph[now]:
        if not chk[next_point]:
            que.append((next_point, min(weight, next_weight)))
            chk[next_point] = True

print(result)
