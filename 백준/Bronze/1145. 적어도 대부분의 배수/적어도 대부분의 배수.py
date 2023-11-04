nums = sorted(list(map(int, input().split())))
ref = nums[2]

while True:
    chk = 0
    for num in nums:
        if ref % num == 0: chk += 1
    if chk > 2:
        print(ref)
        break
    ref += 1