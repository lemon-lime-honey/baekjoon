from collections import defaultdict


def getNumber(n):
    if n not in dp:
        dp[n] = getNumber(n // p) + getNumber(n // q)
    return dp[n]


n, p, q = map(int, input().split())
dp = defaultdict(int)
dp[0] = 1

result = getNumber(n)
print(result)