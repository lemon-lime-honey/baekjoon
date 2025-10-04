l, r, x = map(int, input().split())
nums = [False for i in range(10001)]

for i in range(l, r + 1):
    nums[i | x] = True

for idx, num in enumerate(nums):
    if not num:
        print(idx)
        break
