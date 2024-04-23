import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = [[1 for i in range(k + 1)] for j in range(n + 1)]

for i in range(2, k + 1):
    for j in range(1, n + 1):
        result[j][i] = (result[j][i - 1] + result[j - 1][i]) % int(1e9)

print(result[n][k])