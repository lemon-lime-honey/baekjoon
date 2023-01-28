a, b = map(int, input().split())

if a % b == 0:
    print(a // b)
else:
    print(f'{a // b}.', end = '')
    under = list()
    while True:
        a = (a % b) * 10
        under.append(a // b)
        if a % b == 0:
            break
        if len(under) == 2000:
            break
    print(*under, sep = '')