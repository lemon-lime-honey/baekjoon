def calc(n):
    if n < 10:
        return False

    nums = list()

    while n:
        nums.append(n % 10)
        n //= 10

    f = 1

    for i in range(len(nums) - 1):
        b = 1
        f *= nums[i]

        for j in range(len(nums) - 1, i, -1):
            b *= nums[j]

        if f == b:
            return True

    return False


n = int(input())
print("YES" if calc(n) else "NO")
