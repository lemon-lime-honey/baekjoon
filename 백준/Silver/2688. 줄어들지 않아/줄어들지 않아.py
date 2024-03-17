import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    number = [[0 for j in range(10)] for k in range(n)]

    for j in range(10):
        number[0][j] = 1

    for j in range(1, n):
        for k in range(10):
            for l in range(k, 10):
                number[j][l] += number[j - 1][k]

    print(sum(number[-1]))