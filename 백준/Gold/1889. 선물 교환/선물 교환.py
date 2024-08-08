from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
present = [[] for i in range(n + 1)]
chk = [False for i in range(n + 1)]
deg = [0 for i in range(n + 1)]
result = list()

for i in range(1, n + 1):
    a, b = map(int, input().split())
    present[i] = [a, b]
    deg[a] += 1
    deg[b] += 1

que = deque()

for i in range(1, n + 1):
    if deg[i] < 2:
        que.append(i)
        chk[i] = True

while que:
    now = que.popleft()
    for next_person in present[now]:
        deg[next_person] -= 1
        if deg[next_person] < 2 and not chk[next_person]:
            que.append(next_person)
            chk[next_person] = True

for i in range(1, n + 1):
    if not chk[i]:
        result.append(i)

print(len(result))
print(*result)
