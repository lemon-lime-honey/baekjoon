n = int(input())
nums = list(map(int, input().split()))
result, temp = 0, 0

for num in nums:
    result += num * temp
    temp += num

print(result)
