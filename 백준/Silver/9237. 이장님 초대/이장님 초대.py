n = int(input())
nums = sorted(list(map(int, input().split())), reverse=True)
result = nums[0]

if n != 1:
    for i in range(1, n):
        if result < i + nums[i]:
            result = i + nums[i]

print(result + 2)
