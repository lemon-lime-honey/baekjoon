a, b = map(int, input().split())

print((max(a, b) - min(a, b) + 1) * (a + b) // 2)