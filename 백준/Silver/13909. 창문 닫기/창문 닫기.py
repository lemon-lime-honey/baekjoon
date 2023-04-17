n = int(input())
result = 0

for i in range(1, n + 1):
    if i * i <= n: result += 1
    else: break

print(result)