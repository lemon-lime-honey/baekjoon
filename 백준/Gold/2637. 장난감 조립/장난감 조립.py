from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
parts = [[] for i in range(n + 1)]
deg = [0 for i in range(n + 1)]
result = [0 for i in range(n + 1)]
basic = set()
result[n] = 1

for i in range(m):
    x, y, k = map(int, input().split())
    deg[y] += k
    parts[x].append((y, k))

que = deque([n])

while que:
    now = que.popleft()
    for next_part, amount in parts[now]:
        deg[next_part] -= amount
        result[next_part] += amount * result[now]
        if deg[next_part] == 0:
            que.append(next_part)
        if not parts[next_part]:
            basic.add(next_part)

for i in range(1, n + 1):
    if i in basic:
        print(i, result[i])
