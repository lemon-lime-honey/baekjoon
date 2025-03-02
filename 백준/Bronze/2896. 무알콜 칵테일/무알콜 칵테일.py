a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

num = min(a / i, b / j, c / k)

print(a - num * i, b - num * j, c - num * k)
