import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    ipt = input().rstrip().split()
    result = list()

    for j in range(len(ipt[1])):
        if j == int(ipt[0]) - 1:
            continue
        result.append(ipt[1][j])

    print(''.join(result))