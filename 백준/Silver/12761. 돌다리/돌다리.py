from collections import deque

a, b, n, m = map(int, input().split())

graph = [int(1e12) for i in range(100000 + 1)]
graph[n] = 0

que = deque()
que.append((n + 1, 1))
que.append((n - 1, 1))
que.append((n + a, 1))
que.append((n + b, 1))
que.append((n - a, 1))
que.append((n - b, 1))
que.append((n * a, 1))
que.append((n * b, 1))

while que:
    point, cnt = que.popleft()
    if point < 0 or point > 100000 or graph[point] <= cnt:
        continue

    graph[point] = cnt
    que.append((point + 1, cnt + 1))
    que.append((point - 1, cnt + 1))
    que.append((point + a, cnt + 1))
    que.append((point + b, cnt + 1))
    que.append((point - a, cnt + 1))
    que.append((point - b, cnt + 1))
    que.append((point * a, cnt + 1))
    que.append((point * b, cnt + 1))

print(graph[m])
