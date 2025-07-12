t = int(input())

for i in range(t):
    n = int(input())
    target = n ** 2
    result = True

    while n:
        if n % 10 != target % 10:
            result = False
            break
        n //= 10
        target //= 10

    print("YES" if result else "NO")
