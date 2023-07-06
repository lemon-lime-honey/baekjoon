from collections import deque

def solution(n, vertex):
    graph = [[] for i in range(n + 1)]
    dist = [int(1e9) for i in range(n + 1)]
    que = deque()
    max_dist = 0
    answer = 0

    for x, y in vertex:
        graph[x].append(y)
        graph[y].append(x)

    que.append(1)
    dist[1] = 0

    while que:
        now = que.popleft()
        for next_point in graph[now]:
            if dist[next_point] > dist[now] + 1:
                dist[next_point] = dist[now] + 1
                max_dist = max(max_dist, dist[next_point])
                que.append(next_point)

    for point in dist:
        if point == max_dist:
            answer += 1

    return answer