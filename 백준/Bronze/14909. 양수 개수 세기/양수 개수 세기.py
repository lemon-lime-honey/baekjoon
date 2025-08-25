nums = list(map(int, input().split()))
result = 0

for num in nums:
    if num > 0:
        result += 1

print(result)
