n = int(input())
a = list(map(int, input().split()))
result = [1] * n

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[i] < a[j]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))