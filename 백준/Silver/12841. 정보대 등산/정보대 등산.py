import sys

input = sys.stdin.readline

n = int(input())

cross = list(map(int, input().split()))
left = list(map(int, input().split()))
right = list(map(int, input().split()))

left_prefix = [0 for i in range(n)]
right_prefix = [0 for i in range(n)]

for i in range(1, n):
    left_prefix[i] = left_prefix[i - 1] + left[i - 1]

for i in range(n - 2, -1, -1):
    right_prefix[i] = right_prefix[i + 1] + right[i]

result = [0, int(1e20)]

for i in range(n):
    total = cross[i] + left_prefix[i] + right_prefix[i]
    if total < result[1]:
        result[0] = i + 1
        result[1] = total

print(*result)
