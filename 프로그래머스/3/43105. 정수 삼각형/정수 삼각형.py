def solution(triangle):
    dp = list()

    for nums in triangle:
        if not dp:
            dp.append(nums)
            continue
        temp = [0 for i in range(len(nums))]
        for i in range(len(dp[-1])):
            temp[i] = max(temp[i], dp[-1][i] + nums[i])
            temp[i + 1] = max(temp[i + 1], dp[-1][i] + nums[i + 1])
        dp.append(temp)

    return max(dp[-1])