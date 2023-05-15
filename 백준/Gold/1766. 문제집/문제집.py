import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
problems = [[] for i in range(n + 1)]
chk = [0 for i in range(n + 1)]
result = list()
que = list()

for i in range(m):
    a, b = map(int, input().split())
    problems[a].append(b)
    chk[b] += 1

for i in range(1, n + 1):
    if chk[i] == 0:
        heapq.heappush(que, i)

while que:
    now = heapq.heappop(que)
    result.append(now)
    for problem in problems[now]:
        chk[problem] -= 1
        if chk[problem] == 0:
            heapq.heappush(que, problem)

print(*result)
