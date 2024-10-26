n, d = map(int, input().split())
result = 0

for i in range(1, n + 1):
    num = i
    while num:
        if num % 10 == d:
            result += 1
        num //= 10

print(result)