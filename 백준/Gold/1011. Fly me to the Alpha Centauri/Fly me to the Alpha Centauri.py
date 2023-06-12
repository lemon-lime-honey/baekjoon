t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    dist = y - x
    n = 0

    while True:
        if dist <= n * (n + 1): break
        n += 1

    print(n * 2 - 1 if dist <= n ** 2 else n * 2)