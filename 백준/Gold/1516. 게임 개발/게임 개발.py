from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
buildings = [[] for i in range(n + 1)]
time = [0 for i in range(n + 1)]
deg = [0 for i in range(n + 1)]
dp = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    ipt = list(map(int, input().split()))
    time[i] = ipt[0]
    for num in ipt[1:]:
        if num != -1:
            buildings[num].append(i)
            deg[i] += 1

que = deque()

for i in range(1, n + 1):
    if not deg[i]:
        que.append(i)
        dp[i] = time[i]

while que:
    now = que.popleft()
    for next_point in buildings[now]:
        deg[next_point] -= 1
        dp[next_point] = max(dp[now] + time[next_point], dp[next_point])
        if not deg[next_point]:
            que.append(next_point)

print(*dp[1:], sep='\n')