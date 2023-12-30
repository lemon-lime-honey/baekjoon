t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))
    small = int(1e9)
    total = 0

    for num in nums:
        if not num % 2:
            total += num
            small = min(small, num)

    print(total, small)