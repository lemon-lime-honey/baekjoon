import sys
input = sys.stdin.readline

n, m = map(int, input().split())
costs = sorted([int(input()) for i in range(m)], reverse=True)
result = [0, 0]

for i in range(min(n, m)):
    temp = (i + 1) * costs[i]
    if result[1] < temp:
        result = [costs[i], temp]

print(*result)
