import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]
lis = [0 for i in range(n)]
lds = [0 for i in range(n)]
result = 0

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if nums[i] < nums[j]:
            lis[i] = max(lis[i], lis[j])
        else:
            lds[i] = max(lds[i], lds[j])
    lis[i] += 1
    lds[i] += 1
    result = max(result, lis[i] + lds[i] - 1)

print(result)
