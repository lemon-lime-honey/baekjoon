t = int(input())

for i in range(t):
    result = list()
    n = int(input())

    for j in range(n):
        c, k = map(str, input().split())
        k = int(k)

        for l in range(k):
            result.append(c)

    print(f'#{i + 1}')
    ref = 0

    while ref < len(result):
        print(*result[ref: ref + 10], sep = '')
        ref += 10
