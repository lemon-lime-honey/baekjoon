import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
targets = set(map(int, input().split()))
result = 0

for i in range(m):
    if nums[i] not in targets:
        result += 1

print(result)