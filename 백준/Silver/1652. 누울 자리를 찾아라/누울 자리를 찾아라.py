n = int(input())
space = [[0 for i in range(n)]for j in range(n)]
row = 0
column = 0

for i in range(n):
    space[i] = list(input())
    dot = 0

    for j in range(n):
        if space[i][j] == '.':
            dot += 1
        else:
            if dot >= 2:
                row += 1
            dot = 0
    if dot >= 2:
        row += 1

for i in range(n):
    dot = 0
    for j in range(n):
        if space[j][i] == '.':
            dot += 1
        else:
            if dot >= 2:
                column += 1
            dot = 0
    if dot >= 2:
        column += 1

print(f'{row} {column}')