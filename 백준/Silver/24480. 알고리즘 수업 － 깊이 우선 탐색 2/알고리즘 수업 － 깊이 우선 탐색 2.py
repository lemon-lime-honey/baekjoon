import sys

sys.setrecursionlimit(10 ** 6)

def dfs(s):
    global cnt
    cnt += 1
    visited[s] = True
    result[s] = cnt
    for point in line[s]:
        if not visited[point]:
            dfs(point)

n, m, r = map(int, sys.stdin.readline().split())
line = [[]for i in range(n + 1)]
visited = [True] + [False] * n
result = [0] * (n + 1)
cnt = 0

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    line[u].append(v)
    line[v].append(u)

for i in range(n + 1):
    line[i].sort(reverse = True)

dfs(r)

for i in range(1, n + 1):
    print(result[i])

