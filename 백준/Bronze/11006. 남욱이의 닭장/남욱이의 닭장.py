t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    print(2 * m - n, n - m)
