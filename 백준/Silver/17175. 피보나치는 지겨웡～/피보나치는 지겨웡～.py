n = int(input())
result = [1, 1]

for i in range(2, n + 1):
    result.append((result[-1] + result[-2] + 1) % 1_000_000_007)

print(result[n])
