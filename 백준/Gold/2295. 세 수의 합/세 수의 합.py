from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
u = [int(input()) for i in range(n)]
sums = set()
result = -1

for i in range(n):
    for j in range(n):
        sums.add(u[i] + u[j])

sums = sorted(sums)

for i in range(n):
    for j in range(n):
        idx = bisect_left(sums, u[i] - u[j])
        if sums[idx] == u[i] - u[j]:
            result = max(result, u[i])

print(result)