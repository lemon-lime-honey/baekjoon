def calc():
    for i in range(n - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:
            return sum(nums[i: i + 3])
    return -1


n = int(input())
nums = sorted([int(input()) for i in range(n)], reverse=True)

print(calc())
