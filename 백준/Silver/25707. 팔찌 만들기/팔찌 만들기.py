n = int(input())
nums = sorted(list(map(int, input().split())))
result = nums[-1] - nums[0]

for i in range(1, n):
    result += nums[i] - nums[i - 1]

print(result)
