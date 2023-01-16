while True:
    n = int(input())
    if n == 0:
        break
    total = 0
    while n > 0:
        total += n
        n -= 1
    print(total)