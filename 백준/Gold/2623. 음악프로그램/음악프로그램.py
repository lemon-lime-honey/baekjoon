import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
chk = [0 for i in range(n + 1)]
graph = [[] for i in range(n + 1)]
result = list()
que = deque()

for i in range(m):
    ipt = list(map(int, input().split()))
    for j in range(1, ipt[0]):
        graph[ipt[j]].append(ipt[j + 1])
        chk[ipt[j + 1]] += 1

for i in range(1, n + 1):
    if chk[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    result.append(now)
    for element in graph[now]:
        chk[element] -= 1
        if chk[element] == 0:
            que.append(element)

if len(result) == n:
    print(*result, sep='\n')
else:
    print(0)