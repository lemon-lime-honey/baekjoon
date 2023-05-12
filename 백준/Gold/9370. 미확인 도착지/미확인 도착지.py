import heapq, sys
input = sys.stdin.readline


def dijkstra(p):
    dist = [int(1e9) for j in range(n + 1)]
    dist[p] = 0
    que = [(0, p)]

    while que:
        cost, point = heapq.heappop(que)

        for next_point, next_cost in graph[point]:
            if cost + next_cost < dist[next_point]:
                dist[next_point] = cost + next_cost
                heapq.heappush(que, (cost + next_cost, next_point))
    
    return dist


T = int(input())

for i in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for j in range(n + 1)]

    for j in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    points = [int(input()) for j in range(t)]

    first = dijkstra(s)
    second = dijkstra(g)
    third = dijkstra(h)

    result = list()

    for dest in points:
        if first[g] + second[h] + third[dest] == first[dest] or first[h] + third[g] + second[dest] == first[dest]:
            result.append(dest)

    result.sort()
    print(*result)