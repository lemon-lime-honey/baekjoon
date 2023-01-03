def binomial(n, k):
    if 0 <= k <= n:
        a = 1
        b = 1
        for i in range(1, min(k, n - k) + 1):
            a *= n
            b *= i
            n -= 1
        return a // b
    else:
        return 0
n, k = map(int, input().split())
print(binomial(n, k))