t = int(input())

for i in range(t):
    n = int(input())
    place = list()
    ref = 0

    while n:
        if n % 2:
            place.append(ref)
        n //= 2
        ref += 1

    print(*place)