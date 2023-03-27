import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellman_ford(start):
    route[start - 1] = 0
    for i in range(n):
        for j in range(m):
            point, next_point, cost = bus[j]
            if route[point - 1] != INF and route[point - 1] + cost < route[next_point - 1]:
                route[next_point - 1] = route[point - 1] + cost
                if i == n - 1:
                    return True
    return False

n, m = map(int, input().split())
bus = [list(map(int, input().split())) for i in range(m)]
route = [INF for i in range(n)]

negative = bellman_ford(1)

if negative: print(-1)
else:
    for i in range(1, n):
        if route[i] == INF: print(-1)
        else: print(route[i])