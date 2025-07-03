t = int(input())

for i in range(t):
    ipt = input().split()
    result = list()
    targets = None

    if ipt[1] == "C":
        targets = input().split()
    else:
        targets = list(map(int, input().split()))

    if ipt[1] == "C":
        for target in targets:
            result.append(ord(target) - ord("A") + 1)
    else:
        for target in targets:
            result.append(chr(target + ord("A") - 1))

    print(*result)
