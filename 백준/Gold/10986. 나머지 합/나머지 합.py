n, m = map(int, input().split())
nums = list(map(int, input().split()))
left = [0 for i in range(m)]
left[0] = 1
result = 0
total = 0

for num in nums:
    total += num
    total %= m
    if left[total]: result += left[total]
    left[total] += 1

print(result)