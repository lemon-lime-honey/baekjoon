from collections import deque
import sys, heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
road = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
visited[x] = True
result = list()
que = deque()
que.appendleft((0, x))


for i in range(m):
    a, b = map(int, input().split())
    heapq.heappush(road[a], b)

while que:
    length, city = que.popleft()
    while road[city]:
        temp = heapq.heappop(road[city])
        if visited[temp]: continue
        visited[temp] = True
        que.append((length + 1, temp))
        if length + 1 == k:
            heapq.heappush(result, temp)

if result:
    for i in range(len(result)):
        print(heapq.heappop(result))
else:
    print(-1)