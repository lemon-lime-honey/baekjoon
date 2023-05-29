from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    building = [[] for j in range(n + 1)]
    deg = [0 for j in range(n + 1)]
    dp = [0 for j in range(n + 1)]

    for j in range(k):
        x, y = map(int, input().split())
        building[x].append(y)
        deg[y] += 1

    w = int(input())

    que = deque()
    for j in range(1, n + 1):
        if deg[j] == 0:
            que.append(j)
            dp[j] = time[j]

    while que:
        now = que.popleft()
        for next_point in building[now]:
            deg[next_point] -= 1
            dp[next_point] = max(dp[now] + time[next_point], dp[next_point])
            if deg[next_point] == 0:
                que.append(next_point)

    print(dp[w])