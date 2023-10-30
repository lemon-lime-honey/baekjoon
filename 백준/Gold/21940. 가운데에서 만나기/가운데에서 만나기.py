import sys
input = sys.stdin.readline

n, m = map(int, input().split())
routes = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    routes[i][i] = 0

for i in range(m):
    a, b, t = map(int, input().split())
    routes[a][b] = t

k = int(input())
cities = list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for l in range(1, n + 1):
            if routes[j][l] < routes[j][i] + routes[i][l]:
                continue
            routes[j][l] = routes[j][i] + routes[i][l]

chk = [int(1e9) for i in range(n + 1)]
min_dist = int(1e9)

for i in range(1, n + 1):
    temp = [0 for i in range(k)]
    for j in range(k):
        if (routes[i][cities[j]] != int(1e9) and
            routes[cities[j]][i] != int(1e9)):
            temp[j] +=  routes[i][cities[j]] + routes[cities[j]][i]
    chk[i] = max(temp)
    min_dist = min(min_dist, chk[i])

result = list()

for i in range(1, n + 1):
    if chk[i] == min_dist:
        result.append(i)

print(*result)