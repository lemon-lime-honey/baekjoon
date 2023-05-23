import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [[False for i in range(n)] for j in range(n)]
m = int(input())

for i in range(n):
    dp[i][i] = True

for i in range(n - 1):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = True

for i in range(2, n):
    for j in range(n - i):
        k = j + i
        if numbers[j] == numbers[k] and dp[j + 1][k - 1]:
            dp[j][k] = True

for i in range(m):
    s, e = map(int, input().split())
    print(1 if dp[s - 1][e - 1] else 0)