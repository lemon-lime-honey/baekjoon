n = int(input())
nums = list()

for i in range(n):
    x, y = map(int, input().split())
    nums.append(y)

nums.sort()

print(nums[-1] - nums[0])
