import sys
input = sys.stdin.readline


def bishop(num, cnt, ot):
    if num >= 2 * n - 1:
        if ot:
            global one
            one = max(one, cnt)
        else:
            global two
            two = max(two, cnt)
        return

    flag = False

    for k in range(num, 2 * n - 1, 2):
        for i, j in can[k]:
            if not diag1[i + j] and not diag2[i - j + n - 1]:
                flag = True
                diag1[i + j] = True
                diag2[i - j + n - 1] = True
                bishop(num + 2, cnt + 1, ot)
                diag1[i + j] = False
                diag2[i - j + n - 1] = False

    if not flag: bishop(num + 2, cnt, ot)


n = int(input())
board = list()
diag1 = [False for i in range(2 * n - 1)]
diag2 = [False for i in range(2 * n - 1)]
can = [[] for i in range(2 * n - 1)]
one, two = 0, 0

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j]:
            can[i + j].append((i, j))

bishop(0, 0, True)
bishop(1, 0, False)

print(one + two)