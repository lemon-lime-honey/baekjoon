import heapq, sys
input = sys.stdin.readline

n = int(input())
task = list()
result = int(1e9)

for i in range(n):
    d, t = map(int, input().split())
    heapq.heappush(task, (-t, d))

while task:
    t, d = heapq.heappop(task)
    t = -t
    if result > t:
        result = t - d
    else:
        result -= d

print(result)