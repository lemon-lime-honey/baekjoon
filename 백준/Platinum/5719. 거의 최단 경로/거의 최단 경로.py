from collections import deque
import sys
input = sys.stdin.readline


def dijkstra():
    result = [set() for i in range(n)]
    que = deque([(s, 0)])
    
    while que:
        now, cost = que.popleft()
        if costs[now] < cost: continue
        for next_point, next_cost in roads[now]:
            if next_cost == int(1e9): continue
            if next_cost + costs[now] == costs[next_point]:
                result[next_point].add(now)
            elif next_cost + costs[now] < costs[next_point]:
                costs[next_point] = next_cost + costs[now]
                result[next_point].clear()
                result[next_point].add(now)
                que.append((next_point, next_cost))

    return result


def erase():
    chk = [False for i in range(n)]
    que = deque([d])
    chk[d] = True
    
    while que:
        now = que.popleft()
        for prev in minimum[now]:
            if not chk[prev]:
                chk[prev] = True
                que.append(prev)
            for i in range(len(roads[prev])):
                if roads[prev][i][0] == now:
                    roads[prev][i][1] = int(1e9)


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    s, d = map(int,input().split())
    roads = [[] for i in range(n)]

    for i in range(m):
        u, v, p = map(int, input().split())
        roads[u].append([v, p])

    costs = [int(1e9) for i in range(n)]
    costs[s] = 0
    minimum = dijkstra()

    chk = [False for i in range(n)]
    erase()

    costs = [int(1e9) for i in range(n)]
    costs[s] = 0
    dijkstra()

    print(-1 if costs[d] == int(1e9) else costs[d])