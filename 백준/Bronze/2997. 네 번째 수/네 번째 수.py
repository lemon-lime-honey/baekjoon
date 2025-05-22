nums = sorted(list(map(int, input().split())))

if nums[1] - nums[0] == nums[2] - nums[1]:
    print(nums[2] + nums[1] - nums[0])
elif nums[1] - nums[0] == 2 * (nums[2] - nums[1]):
    print(nums[0] + nums[2] - nums[1])
elif 2 * (nums[1] - nums[0]) == nums[2] - nums[1]:
    print(2 * nums[1] - nums[0])
