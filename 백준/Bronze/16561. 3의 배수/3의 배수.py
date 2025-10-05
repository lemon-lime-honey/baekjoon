n = int(input())
result = 0

for i in range(3, max(n - 6, 0) + 1, 3):
    for j in range(i + 3, max(n - 3, 0) + 1, 3):
        result += 1

print(result)
