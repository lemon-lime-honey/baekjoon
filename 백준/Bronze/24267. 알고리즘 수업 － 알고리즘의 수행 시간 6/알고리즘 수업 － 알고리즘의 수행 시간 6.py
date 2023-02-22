n = int(input())
result = 0
for i in range(1, n - 1):
    result += i * (n - 1 - i)

print(result, 3, sep = '\n')