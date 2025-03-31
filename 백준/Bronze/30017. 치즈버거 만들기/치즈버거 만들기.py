a, b = map(int, input().split())

if a > b:
    print(2 * b + 1)
else:
    print(max(2 * a - 1, 0))
