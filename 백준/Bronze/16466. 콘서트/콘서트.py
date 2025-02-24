n = int(input())
nums = list(map(int, input().split()))

result = 1

nums.sort()

for num in nums:
    if num == result:
        result += 1
    else:
        break

print(result)
