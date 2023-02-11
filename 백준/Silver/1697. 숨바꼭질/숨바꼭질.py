from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
points = deque([n])

while points:
    now = points.popleft()

    if (now == k):
        break
    if (0 <= now - 1 <= 100000) and not visited[now - 1]:
        points.append(now - 1)
        visited[now - 1] = visited[now] + 1
    if (0 <= now + 1 <= 100000) and not visited[now + 1]:
        points.append(now + 1)
        visited[now + 1] = visited[now] + 1
    if (0 < now * 2 <= 100000) and not visited[now * 2]:
        points.append(now * 2)
        visited[now * 2] = visited[now] + 1

print(visited[k])