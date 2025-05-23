def calc(num):
    if num >= 300:
        return 1
    elif num >= 275:
        return 2
    elif num >= 250:
        return 3
    return 4

n = int(input())
nums = list(map(int, input().split()))
result = list()

for level in nums:
    result.append(calc(level))

print(*result)
