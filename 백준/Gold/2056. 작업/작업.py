from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
works = [[] for i in range(n + 1)]
time = [0 for i in range(n + 1)]
deg = [0 for i in range(n + 1)]
dp = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    ipt = list(map(int, input().split()))
    time[i] = ipt[0]
    for num in ipt[1:]:
        if not num: continue
        works[num].append(i)
        deg[i] += 1

que = deque()

for i in range(1, n + 1):
    if not deg[i]:
        que.append(i)
        dp[i] = time[i]

while que:
    now = que.popleft()
    for next_work in works[now]:
        dp[next_work] = max(dp[now] + time[next_work], dp[next_work])
        deg[next_work] -= 1
        if not deg[next_work]:
            que.append(next_work)

print(max(dp))