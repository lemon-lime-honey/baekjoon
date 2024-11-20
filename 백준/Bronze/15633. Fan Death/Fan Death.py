n = int(input())
result = 0

for i in range(1, n + 1):
    if not n % i:
        result += i

print(result * 5 - 24)