t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    result = [0 for j in range((n))]
    num = 1

    for j in range(n):
        if nums[j] != num:
            result[j] = num
            num += 1
        else:
            result[j] = num + 1
            num += 2

    print(result[-1])
