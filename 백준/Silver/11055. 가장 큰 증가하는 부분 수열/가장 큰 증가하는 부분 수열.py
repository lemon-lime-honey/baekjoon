n = int(input())
numbers = list(map(int, input().split()))
dp = [numbers[i] for i in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

print(max(dp))