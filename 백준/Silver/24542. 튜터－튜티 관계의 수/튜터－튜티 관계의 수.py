from collections import deque
import sys

input = sys.stdin.readline


def bfs(idx):
    que = deque([idx])
    chk[idx] = True
    cnt = 1

    while que:
        now = que.popleft()
        for next_point in graph[now]:
            if chk[next_point]:
                continue
            que.append(next_point)
            chk[next_point] = True
            cnt += 1

    return cnt


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
chk = [False for i in range(n + 1)]
result = 1

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if chk[i]:
        continue
    result *= bfs(i)
    result %= 1000000007

print(result)
