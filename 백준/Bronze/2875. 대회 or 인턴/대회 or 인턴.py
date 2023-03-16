n, m, k = map(int, input().split())
result = 0

while True:
    n -= 2
    m -= 1
    if n < 0 or m < 0 or (n + m) < k:
        break
    result += 1

print(result)