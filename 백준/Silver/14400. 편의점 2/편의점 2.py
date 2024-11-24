import sys

input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for i in range(n)]
result = 0

points.sort(key=lambda x: x[0])

X = points[(n - 1) // 2][0]

points.sort(key=lambda x: x[1])

Y = points[(n - 1) // 2][1]

for x, y in points:
    result += abs(X - x) + abs(Y - y)

print(result)
