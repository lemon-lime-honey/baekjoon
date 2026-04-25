n, m, s = map(int, input().split())

print(min(int(s * (100 - n) * (m + 1) / 100), s * m))
