r, g, b = map(int, input().split())
result = 0

result += r // 3 + g // 3 + b // 3
r, g, b = r % 3, g % 3, b % 3

while r > 0 and g > 0 and b > 0:
    result += 1
    r, g, b = r - 1, g - 1, b - 1

while r > 0 and g > 0:
    result += 1
    r, g = r - 1, g - 1

while r > 0 and b > 0:
    result += 1
    r, b = r - 1, b - 1

while g > 0 and b > 0:
    result += 1
    g, b = g - 1, b - 1

result += 1 * (r > 0) + 1 * (g > 0) + 1 * (b > 0)

print(result)
