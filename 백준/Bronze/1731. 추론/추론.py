import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]

if nums[1] - nums[0] == nums[2] - nums[1]:
    print(nums[-1] + nums[1] - nums[0])
else:
    print(nums[-1] * nums[1] // nums[0])
