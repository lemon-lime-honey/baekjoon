k, n = map(int, input().split())

if n != 1:
    res = n * k // (n - 1)
    if ((n * k) % (n - 1)):
        res += 1
    print(res)
else:
    print(-1)
