import sys

input = sys.stdin.readline

while True:
    ipt = sorted(list(map(int, input().split())))
    result = 0

    if len(ipt) == 1 and ipt[0] == -1:
        break

    flag = False

    for i in range(len(ipt) - 1):
        for j in range(i + 1, len(ipt)):
            if ipt[i] * 2 == ipt[j]:
                result += 1
                break
        if flag:
            break

    print(result)
