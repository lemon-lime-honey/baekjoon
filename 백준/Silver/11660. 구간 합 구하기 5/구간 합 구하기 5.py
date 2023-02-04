import sys

n, m = map(int, sys.stdin.readline().split())
number = [[0 for i in range(n)]for j in range(n)]
sum_list = [[0 for i in range(n)]for j in range(n)]

for i in range(n):
    number[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if not i:
            sum_list[i][j] = number[i][j]
        else:
            sum_list[i][j] = sum_list[i - 1][j] + number[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = 0

    for j in range(y1 - 1, y2):
        result += sum_list[x2 - 1][j] - sum_list[x1 - 1][j] + number[x1 - 1][j]
    
    print(result)