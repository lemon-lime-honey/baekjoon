while True:
    ipt = list(map(int, input().split()))

    if ipt[0] == 0:
        break

    result = list()

    for i in range(1, ipt[0] + 1):
        if not result or ipt[i] != result[-1]:
            result.append(ipt[i])

    print(*result, "$")
