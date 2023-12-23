nums = [False for i in range(10001)]

for i in range(1, 101):
    nums[i * i] = True

m = int(input())
n = int(input())
result = [0, 10001]

for i in range(m, n + 1):
    if nums[i]:
        result[0] += i
        result[1] = min(result[1], i)

if result[0] == 0:
    print(-1)
else:
    print(*result, sep='\n')