n = int(input())
nums = list(map(int, input().split()))
idx = 1
result = 0

for num in nums:
    if num != idx:
        result += 1
    idx += 1

print(result)