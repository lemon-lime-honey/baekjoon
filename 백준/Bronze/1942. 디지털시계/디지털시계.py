for i in range(3):
    ipt = input().split()
    start = list(map(int, ipt[0].split(':')))
    end = list(map(int, ipt[1].split(':')))
    result = 0

    while True:
        if not sum(start) % 3:
            result += 1

        if start == end:
            break

        start[2] += 1
        if start[2] > 59:
            start[2] -= 60
            start[1] += 1
        if start[1] > 59:
            start[1] -= 60
            start[0] += 1
        if start[0] > 23:
            start[0] -= 24

    print(result)