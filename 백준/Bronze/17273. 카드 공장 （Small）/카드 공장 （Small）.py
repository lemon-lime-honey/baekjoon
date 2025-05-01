n, m = map(int, input().split())
card = [True for i in range(n)]
nums = [list(map(int, input().split())) for i in range(n)]
result = 0

for i in range(m):
    k = int(input())
    for j in range(n):
        if card[j]:
            if nums[j][0] <= k:
                card[j] = False
        else:
            if nums[j][1] <= k:
                card[j] = True

for i in range(n):
    if card[i]:
        result += nums[i][0]
    else:
        result += nums[i][1]

print(result)
