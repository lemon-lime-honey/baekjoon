n, m = map(int, input().split())

result = n // m

if n % m:
    result += 1

print(result)
