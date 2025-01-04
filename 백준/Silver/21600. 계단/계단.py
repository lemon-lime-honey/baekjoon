import sys

input = sys.stdin.readline

n = int(input())
histogram = list(map(int, input().split()))
result, height = 0, 0

for i in range(n):
    if height + 1 <= histogram[i]:
        height += 1
        result = max(result, height)
    else:
        height = histogram[i]

print(result)
