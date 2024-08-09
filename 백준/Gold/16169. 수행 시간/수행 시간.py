from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
result = [0 for i in range(n + 1)]
graph = [[] for i in range(n + 1)]
level = [[] for i in range(n + 1)]
time = [0 for i in range(n + 1)]
deg = [0 for i in range(n + 1)]
que = deque()

for i in range(1, n + 1):
    ipt = list(map(int, input().split()))
    level[ipt[0]].append(i)
    time[i] = ipt[1]

for i in range(1, n):
    for j in range(len(level[i])):
        for k in range(len(level[i + 1])):
            deg[level[i + 1][k]] += 1
            graph[level[i][j]].append(level[i + 1][k])

for i in range(1, n + 1):
    if deg[i] == 0:
        que.append((i, time[i]))
        result[i] = time[i]

while que:
    point, cost = que.popleft()
    for next_point in graph[point]:
        next_cost = (point - next_point) ** 2 + cost
        result[next_point] = max(result[next_point], next_cost + time[next_point])
        deg[next_point] -= 1
        if deg[next_point] == 0:
            que.append((next_point, result[next_point]))

print(max(result))
