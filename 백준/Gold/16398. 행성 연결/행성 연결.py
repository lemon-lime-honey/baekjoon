import sys
input = sys.stdin.readline


def find(p):
    if p != planets[p]:
        planets[p] = find(planets[p])
    return planets[p]


def union(p1, p2):
    p1, p2 = find(p1), find(p2)
    if p1 == p2: return
    if p1 < p2: planets[p2] = p1
    else: planets[p1] = p2


n = int(input())
raw_cost = [list(map(int, input().split())) for i in range(n)]
planets = [i for i in range(n)]
costs = list()
result = 0

for i in range(n):
    for j in range(i + 1, n):
        costs.append((raw_cost[i][j], i, j))

costs.sort()

for cost, start, end in costs:
    if find(start) != find(end):
        union(start, end)
        result += cost

print(result)