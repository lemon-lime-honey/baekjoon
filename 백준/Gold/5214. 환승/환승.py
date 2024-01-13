from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [int(1e9) for i in range(n + m + 1)]
    que = deque([1])
    visited[1] = 1
    
    while que:
        now = que.popleft()
        if now == n: return visited[n]
        for station in stations[now]:
            if station < n + 1:
                if visited[station] <= visited[now] + 1: continue
                visited[station] = visited[now] + 1
                que.append(station)
            else:
                visited[station] = visited[now]
                que.append(station)

    return -1


n, k, m = map(int, input().split())
stations = [[] for i in range(n + m + 1)]

for i in range(m):
    ipt = list(map(int, input().split()))
    stations[i + n + 1] = ipt
    for j in range(k):
        stations[ipt[j]].append(i + n + 1)

print(bfs())