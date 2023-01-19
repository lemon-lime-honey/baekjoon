from math import ceil

n, a, b, c, d = map(int, input().split())
x = ceil(n / a) * b
y = ceil(n / c) * d
print(min(x, y))