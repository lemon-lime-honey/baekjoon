n = int(input())
result = list()

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(10):
        if nums[j] != (j % 5) + 1:
            break
    else:
        result.append(i + 1)

result.sort()

print(*result, sep="\n")
