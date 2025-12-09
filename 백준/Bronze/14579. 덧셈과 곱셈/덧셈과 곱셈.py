a, b = map(int, input().split())

result = 1

for i in range(a, b + 1):
    result *= (i + 1) * i // 2
    result %= 14579

print(result)
