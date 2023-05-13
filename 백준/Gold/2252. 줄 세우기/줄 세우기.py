import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
chk = [0 for i in range(n + 1)]
result = list()
que = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    chk[b] += 1

for i in range(1, n + 1):
    if chk[i] == 0:
        que.append(i)

while que:
    temp = que.popleft()
    result.append(temp)
    for target in graph[temp]:
        chk[target] -= 1
        if chk[target] == 0:
            que.append(target)

print(*result)