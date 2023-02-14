n, m = map(int, input().split())

large = max(m, n - m)
small = min(m, n - m)

result = 1

while n:
    if n > large:
        result *= n
    elif small >= n:
        result //= n
    n -= 1

print(result)