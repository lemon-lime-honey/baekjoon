from collections import defaultdict
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for i in range(5)]
call = list()
result = 0

ver = defaultdict(int)
hor = defaultdict(int)
diag1 = defaultdict(int)
diag2 = defaultdict(int)

for i in range(5):
    call.extend(list(map(int, input().split())))

for number in call:
    result += 1
    flag = False
    cnt = 0

    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                ver[i] += 1
                hor[j] += 1
                diag1[i - j] += 1
                diag2[i + j] += 1

                flag = True
                break
        if flag: break

    for item, value in ver.items():
        if value == 5: cnt += 1
    for item, value in hor.items():
        if value == 5: cnt += 1
    for item, value in diag1.items():
        if value == 5: cnt += 1
    for item, value in diag2.items():
        if value == 5: cnt += 1

    if cnt > 2:
        print(result)
        sys.exit()