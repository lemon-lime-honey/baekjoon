n = int(input())
result = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if i + j + k != n:
                continue
            if k % 2:
                continue
            if j < i + 2:
                continue
            result += 1

print(result)
