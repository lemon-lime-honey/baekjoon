t = int(input())

for i in range(t):
    d, n, s, p = map(int, input().split())
    parallel = d + n * p
    serial = n * s

    if parallel < serial:
        print("parallelize")
    elif parallel == serial:
        print("does not matter")
    else:
        print("do not parallelize")
