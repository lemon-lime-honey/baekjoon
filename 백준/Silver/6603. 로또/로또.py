def choice(n):
    if len(n) == 6:
        result.add(tuple(sorted(n)))
        return
    for i in range(k):
        if number[i] not in n:
            n.append(number[i])
            choice(n)
            n.pop()
    return


while True:
    ipt = list(map(int, input().split()))
    if len(ipt) == 1: break
    number = ipt[1:]
    k = ipt[0]
    result = set()
    choice(list())
    answer = sorted(list(result))
    for numbers in answer:
        print(*numbers)
    print()