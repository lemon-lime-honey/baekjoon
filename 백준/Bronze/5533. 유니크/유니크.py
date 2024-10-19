n = int(input())
nums = [list(map(int, input().split())) for i in range(n)]

for i in range(3):
    score = [0 for j in range(n)]

    for j in range(n):
        score[j] = nums[j][i]
        for k in range(n):
            if k != j and nums[k][i] == score[j]:
                score[j] = 0
                break

    for j in range(n):
        nums[j][i] = score[j]

result = [0 for i in range(n)]

for i in range(n):
    result[i] = sum(nums[i])

print(*result, sep="\n")
