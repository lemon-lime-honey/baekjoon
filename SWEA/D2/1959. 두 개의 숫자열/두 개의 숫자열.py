t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = list()

    if n < m:
        for j in range(m - n + 1):
            temp = 0
            for k in range(j, j + n):
                    temp += a[k - j] * b[k]
            result.append(temp)
    else:
        for j in range(n - m + 1):
            temp = 0
            for k in range(j, j + m):
                temp += a[k] * b[k - j]
            result.append(temp)

    print(f'#{i + 1} {max(result)}')