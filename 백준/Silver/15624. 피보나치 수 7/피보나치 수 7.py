n = int(input())

if n == 0:
    print(0)
else:
    nums = [0, 1]

    for i in range(n - 1):
        nums[0], nums[1] = nums[1], (nums[0] + nums[1]) % 1_000_000_007

    print(nums[1])
