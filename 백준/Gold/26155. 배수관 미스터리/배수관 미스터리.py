import heapq, sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(p):
    if pipe[p] == p:
        return p
    pipe[p] = find(pipe[p])
    return pipe[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q:
        return False
    if p < q:
        pipe[q] = p
    else:
        pipe[p] = q
    return True


n, m = map(int, input().split())
connections = list()

for i in range(m):
    a, b, p = input().split()
    heapq.heappush(connections, (-float(p), int(a), int(b)))

q = int(input())
queries = list()
result = [0 for i in range(q)]
pipe = [i for i in range(n + 1)]
groups = n

for i in range(q):
    p = float(input())
    heapq.heappush(queries, (-p, i))

for i in range(q):
    query, idx = heapq.heappop(queries)
    query *= -1

    while connections and query <= -connections[0][0]:
        if union(connections[0][1], connections[0][2]):
            groups -= 1
        heapq.heappop(connections)

    result[idx] = groups

print(*result, sep="\n")
