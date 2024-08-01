import sys

input = sys.stdin.readline

t = int(input())
result = list()

for i in range(t):
    n = int(input())
    robots = [input().rstrip() for j in range(n)]
    win = [True for j in range(n)]

    for j in range(len(robots[0])):
        data = [0 for k in range(3)]
        for k in range(n):
            if not win[k]:
                continue
            match robots[k][j]:
                case "S":
                    data[0] = 1
                case "R":
                    data[1] = 1
                case "P":
                    data[2] = 1
        if sum(data) == 2:
            if data[0] == 0: target = "R"
            elif data[1] == 0: target = "P"
            elif data[2] == 0: target = "S"

            for k in range(n):
                if robots[k][j] == target:
                    win[k] = False

    chk, winner = 0, 0

    for j in range(n):
        if win[j]:
            chk += 1
            winner = j + 1

    if chk != 1: result.append(0)
    else: result.append(winner)

print(*result, sep="\n")
