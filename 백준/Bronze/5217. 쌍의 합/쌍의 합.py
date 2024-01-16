import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    result = list()

    for j in range(1, n):
        for k in range(j + 1, n):
            if j + k == n:
                result.append((j, k))

    print(f'Pairs for {n}:', end=' ')

    if not result: print()
    else:
        for j in range(len(result)):
            if j == len(result) - 1:
                print(*result[j])
            else:
                print(*result[j], end=', ')