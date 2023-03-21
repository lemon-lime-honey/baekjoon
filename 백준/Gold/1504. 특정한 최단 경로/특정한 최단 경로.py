import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [int(1e9) for i in range(n + 1)]
    que = list()
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que:
        length, point = heapq.heappop(que)

        if length > distance[point]: continue
        for element in graph[point]:
            next_length, next_point = element
            if length + next_length < distance[next_point]:
                distance[next_point] = length + next_length
                heapq.heappush(que, (length + next_length, next_point))
    
    return distance

n, e = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

one, two = map(int, input().split())

front = dijkstra(1)
middle = dijkstra(one)
back = dijkstra(two)

if front[one] == int(1e9) or middle[two] == int(1e9) or back[n] == int(1e9):
    print(-1)
else:
    if (front[two] + middle[two] + middle[n]) < (front[one] + middle[two] + back[n]):
        print(front[two] + middle[two] + middle[n])
    else:
        print(front[one] + middle[two] + back[n])