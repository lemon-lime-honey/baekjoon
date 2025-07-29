nums = list(map(int, input().split()))
nums.sort()

print(min(nums[0], nums[1]) * min(nums[2], nums[3]))