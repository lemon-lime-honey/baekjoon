from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end = ' ')

    for i in range(1, n + 1):
        if not visited[i] and link[start][i]:
            dfs(i)

def bfs(start):
    visited = [True] + [False] * n
    result = list()
    que = deque([start])

    while que:
        now = que.popleft()

        if not visited[now]:
            visited[now] = True
            result.append(now)
            for i in range(1, n + 1):
                if link[now][i] and i not in que:
                    que.append(i)
    
    return result

n, m, v = map(int, input().split())
link = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    link[x][y] = link[y][x] = 1

visited = [True] + [False] * (n)

dfs(v)
print()
print(*bfs(v))