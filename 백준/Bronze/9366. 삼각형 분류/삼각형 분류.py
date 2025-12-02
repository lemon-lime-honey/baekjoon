t = int(input())

for i in range(1, t + 1):
    nums = list(map(int, input().split()))
    nums.sort()

    if nums[2] >= nums[0] + nums[1]:
        print(f"Case #{i}: invalid!")
    elif nums[0] == nums[1] == nums[2]:
        print(f"Case #{i}: equilateral")
    elif nums[0] == nums[1] or nums[1] == nums[2]:
        print(f"Case #{i}: isosceles")
    else:
        print(f"Case #{i}: scalene")
