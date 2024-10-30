n = int(input())
x_min, x_max, y_min, y_max = 50, 0, 50, 0

for i in range(n):
    x, y = map(int, input().split())
    x_max = max(x, x_max)
    x_min = min(x, x_min)
    y_max = max(y, y_max)
    y_min = min(y, y_min)

print((x_max - x_min + y_max - y_min) * 2)
