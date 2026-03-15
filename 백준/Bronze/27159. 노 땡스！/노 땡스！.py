n = int(input())
nums = list(map(int, input().split()))
result = nums[0]

for i in range(1, n):
    if nums[i - 1] + 1 != nums[i]:
        result += nums[i]

print(result)
