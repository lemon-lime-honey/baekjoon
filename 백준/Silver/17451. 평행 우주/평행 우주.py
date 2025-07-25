n = int(input())
nums = list(map(int, input().split()))

result = nums[-1]

for i in range(n - 2, -1, -1):
    if nums[i] > result:
        result = nums[i]
    elif result % nums[i] != 0:
        result = (result // nums[i] + 1) * nums[i]

print(result)
