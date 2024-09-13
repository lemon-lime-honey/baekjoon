n, k = map(int, input().split())
nums = list(map(int, input().split(',')))
result = [[0 for i in range(n)] for j in range(k + 1)]
result[0] = nums

for i in range(1, k + 1):
    for j in range(n - i):
        result[i][j] = result[i - 1][j + 1] - result[i - 1][j]

print(*result[-1][:n - k], sep=',')
