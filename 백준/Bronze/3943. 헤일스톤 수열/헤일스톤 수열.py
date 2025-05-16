t = int(input())

for i in range(t):
    n = int(input())
    result = n

    while n != 1:
        if n % 2:
            n = (n * 3) + 1
            result = max(result, n)
        else:
            n //= 2

    print(result)
