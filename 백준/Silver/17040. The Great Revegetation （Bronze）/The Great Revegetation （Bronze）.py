import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    seen = [False for i in range(5)]

    for chk in graph[i]:
        if result[chk] != 0:
            seen[result[chk]] = True

    for seed in range(1, 5):
        if not seen[seed]:
            result[i] = seed
            break

print("".join(map(str, result[1:])))
