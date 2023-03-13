n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
result = list()

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

answer = max(dp)
print(answer)

for i in range(n):
    if dp[i] == answer:
        result.append(a[i])
        answer -= 1

print(*result)