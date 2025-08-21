while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(min(2 * a - b, 2 * b - a, (a + b) // 2))
