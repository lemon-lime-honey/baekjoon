import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    last = list(map(int, input().split()))
    graph = [[] for j in range(n + 1)]
    chk = [0 for j in range(n + 1)]
    result = list()
    que = deque()

    for j in range(n):
        graph[last[j]] = last[j + 1:]
        chk[last[j]] = j
    
    m = int(input())

    for j in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].remove(a)
            chk[a] -= 1
            graph[a].append(b)
            chk[b] += 1
        else:
            graph[a].remove(b)
            chk[b] -= 1
            graph[b].append(a)
            chk[a] += 1

    for j in range(1, n + 1):
        if chk[j] == 0:
            que.append(j)
    
    if not que:
        print("IMPOSSIBLE")
        continue

    while que:
        now = que.popleft()
        result.append(now)
        for element in graph[now]:
            chk[element] -= 1
            if chk[element] == 0:
                que.append(element)
    
    if len(result) < n:
        print('IMPOSSIBLE')
    else:
        print(*result)