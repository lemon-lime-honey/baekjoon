import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def dfs(target, weight):
    for element, cost in tree[target]:
        if dist[element] == -1:
            dist[element] = weight + cost
            dfs(element, weight + cost)


n = int(input())
tree = [[] for i in range(n + 1)]

for i in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

dist = [-1 for i in range(n + 1)]
dist[1] = 0
dfs(1, 0)
point = dist.index(max(dist))
dist = [-1 for i in range(n + 1)]
dist[point] = 0
dfs(point, 0)

print(max(dist))