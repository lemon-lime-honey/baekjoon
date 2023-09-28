t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))
    a = float(nums[1] - nums[0])
    b = float(nums[2] - nums[1])
    c = (nums[2] + nums[0]) / 2

    result = min(
        abs(nums[2] - (nums[1] + a)),
        abs(nums[0] - (nums[1] - b)),
        abs(nums[1] - c)
    )
    print(f'#{i + 1} {result}')