n, m, k = map(int, input().split())
small, big = n - m * k, n - (m * (k - 1) + 1)
print(max(0, small), max(0, big))
