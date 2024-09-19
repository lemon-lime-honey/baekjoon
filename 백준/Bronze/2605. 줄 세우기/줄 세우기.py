n = int(input())
nums = list(map(int, input().split()))
result = list()

for idx, num in enumerate(nums):
    if not result:
        result.append(idx + 1)
    else:
        result.insert(len(result) - num, idx + 1)

print(*result)
