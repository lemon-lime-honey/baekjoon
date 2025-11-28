row, col = map(int, input().split())
maps = [input() for i in range(row)]
result = [0, 0, 0, 0, 0]

for r in range(row - 1):
    for c in range(col - 1):
        if maps[r][c] == "#":
            continue
        if maps[r + 1][c] == "#":
            continue
        if maps[r][c + 1] == "#":
            continue
        if maps[r + 1][c + 1] == "#":
            continue

        cnt = 0

        for i in range(2):
            for j in range(2):
                if maps[r + i][c + j] == "X":
                    cnt += 1

        result[cnt] += 1

print(*result, sep="\n")
