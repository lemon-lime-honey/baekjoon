from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
deg = [0 for i in range(n + 1)]
result = [0 for i in range(n + 1)]
subject = [[] for i in range(n + 1)]
que = deque()

for i in range(m):
    a, b = map(int, input().split())
    deg[b] += 1
    subject[a].append(b)

for i in range(1, n + 1):
    if not deg[i]:
        que.append(i)
        result[i] = 1

while que:
    now = que.popleft()
    for s in subject[now]:
        if deg[s] > 0:
          deg[s] -= 1
          if not deg[s]:
              que.append(s)
              result[s] = result[now] + 1

print(*result[1:])