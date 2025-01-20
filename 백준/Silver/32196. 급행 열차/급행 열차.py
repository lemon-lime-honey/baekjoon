import heapq, sys

input = sys.stdin.readline

n, m, k, x, y = map(int, input().split())
lines = list()
result = k * (x + y)

for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(lines, a * x - b * y)

for i in range(m):
    result += heapq.heappop(lines)

print(result)
