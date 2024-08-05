n, a, b = map(int, input().split())
result = 0

while a != b:
    a -= a // 2
    b -= b // 2
    result += 1

print(result)
