t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    result = 0

    for i in range(1, n):
        for j in range(i + 1, n):
            if not (i ** 2 + j ** 2 + m) % (i * j): result += 1

    print(result)