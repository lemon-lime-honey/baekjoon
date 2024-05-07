import sys
input = sys.stdin.readline

n = int(input())
pillars = [0 for i in range(1001)]
tallest = 0
result = 0
idx = 0

for i in range(n):
    l, h = map(int, input().split())
    pillars[l] = h
    if tallest < h:
        tallest = h
        idx = l

height = 0

for i in range(idx + 1):
    height = max(height, pillars[i])
    result += height

height = 0

for i in range(1000, idx, -1):
    height = max(height, pillars[i])
    result += height

print(result)