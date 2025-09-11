while True:
    n = int(input())

    if n == 0:
        break

    result = 0

    while n:
        result += n * n
        n -= 1

    print(result)
