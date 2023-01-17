a, b = map(int, input().split())
case1 = abs(a * (b // 2) - a * (b - b // 2))
case2 = abs(b * (a // 2) - b * (a - a // 2))

if case1 < case2:
    print(case1)
else:
    print(case2)