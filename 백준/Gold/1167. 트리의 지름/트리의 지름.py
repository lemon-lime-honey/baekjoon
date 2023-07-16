from collections import deque

import sys
input = sys.stdin.readline


def bfs(target, weight):
    que = deque()
    que.append((target, weight))

    while que:
        now, cost = que.popleft()
        for next_point, next_cost in tree[now]:
            if dist[next_point] == -1:
                dist[next_point] = cost + next_cost
                que.append((next_point, cost + next_cost))


v = int(input())
tree = [[] for i in range(v + 1)]

for i in range(v):
    ipt = list(map(int, input().split()))
    for j in range(1, len(ipt) - 1, 2):
        tree[ipt[0]].append((ipt[j], ipt[j + 1]))
        tree[ipt[j]].append((ipt[0], ipt[j + 1]))

dist = [-1 for i in range(v + 1)]
dist[1] = 0
bfs(1, 0)
point = dist.index(max(dist))
dist = [-1 for i in range(v + 1)]
dist[point] = 0
bfs(point, 0)

print(max(dist))