nums = list(map(int, input().split()))
nums.sort()

a = nums[0]
bpc = nums[-1] - a
b, c = 0, 0

for num in nums[1:-1]:
    if num < bpc and bpc - num in nums[1:-1]:
        print(a, num, bpc - num)
        break