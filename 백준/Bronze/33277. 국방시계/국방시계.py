n, m = map(int, input().split())
target = 24 * 60 * m // n

if m == n:
    print("24:00")
else:
    print(f"{target // 60:02d}:{target % 60:02d}")
