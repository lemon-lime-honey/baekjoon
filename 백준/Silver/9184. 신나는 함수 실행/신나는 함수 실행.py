import sys

number = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if not i or not j or not k:
                number[i][j][k] = 1
            elif (i < j) and (j < k):
                number[i][j][k] = number[i][j][k - 1] + number[i][j - 1][k - 1] - number[i][j - 1][k]
            else:
                number[i][j][k] = number[i - 1][j][k] + number[i - 1][j - 1][k] + number[i - 1][j][k - 1] - number[i - 1][j - 1][k - 1]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    if (a <= 0) or (b <= 0) or (c <= 0):
        sys.stdout.write(f'w({a}, {b}, {c}) = {number[0][0][0]}\n')
    elif (a > 20) or (b > 20) or (c > 20):
        sys.stdout.write(f'w({a}, {b}, {c}) = {number[20][20][20]}\n')
    else:
        sys.stdout.write(f'w({a}, {b}, {c}) = {number[a][b][c]}\n')