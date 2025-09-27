a, b, c, x, y = map(int, input().split())

result = 0

if 2 * c < a + b:
    result += min(x, y) * 2 * c
    if x < y:
        if b < 2 * c:
            result += b * (y - x)
        else:
            result += 2 * c * (y - x)
    elif x > y:
        if a < 2 * c:
            result += a * (x - y)
        else:
            result += 2 * c * (x - y)
else:
    result = a * x + b * y

print(result)
