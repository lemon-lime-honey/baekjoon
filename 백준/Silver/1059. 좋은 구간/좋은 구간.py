l = int(input())
nums = sorted(list(map(int, input().split())))
n = int(input())

if n in nums:
    print(0)
else:
    start, end = 0, nums[-1]

    for num in nums:
        if num < n and num > start:
            start = num
        elif num > n and num < end:
            end = num

    print((n - start) * (end - n) - 1)
