a, b = map(int, input().split())

if a**2 == b:
    print(-a)
else:
    span = int((a**2 - b) ** 0.5)
    result = sorted([-a + span, -a - span])
    print(*result)
