while True:
    try:
        nums = list(map(int, input().split()))
        nums.sort()
        result = -1

        while nums[0] < nums[1] < nums[2]:
            if nums[1] - nums[0] < nums[2] - nums[1]:
                nums[0], nums[1] = nums[1], nums[2] - 1
            else:
                nums[1], nums[2] = nums[0] + 1, nums[1]
            result += 1

        print(result)
    except Exception:
        break
